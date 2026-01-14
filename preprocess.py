from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions  import OutputParserException
from llm_helper import llm


import json
def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, "r", encoding="utf-8") as file:
        posts= json.load(file)
        print(posts)
        for post in posts:
            metadata= extract_metadata(post['text'])
            post_with_metadata= post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags= get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags= post['tags']   
        new_tags={unified_tags[tag] for tag in current_tags if tag in unified_tags} 
        post['tags']= list(new_tags)

    with open(processed_file_path, "w", encoding="utf-8") as outfile:
        json.dump(enriched_posts, outfile, indent=4)



def get_unified_tags(post_with_metadata):
    unique_tags= set()
    for post in post_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list= ','.join(unique_tags)
    template= '''You are given a list of tags separated by commas. You need to group similar tags and return a mapping of original tag to unified tag.
    1. Return a valid json. No preamble.
    2. The json should have original tags as keys and unified tags as values.
    3. Unified tags should follow title case format.
    4. output should have mapping of original tag and unified tag. for example: {{"jobseekers": "Job Search", "job hunting": "Job Search", "motivation": "Motivation"}}
    here is the list of tags: {tags}'''

    pt= PromptTemplate.from_template(template)
    chain= pt | llm
    response= chain.invoke(input={'tags': str(unique_tags_list)}) 

    try:
        json_parser= JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Failed to parse LLM output to JSON")

    return res  

    

def extract_metadata(post):
    template = '''You are given a linkedin post. you need to extract number of lines, language of the post, and relevant tags from the post.
     1. Reurn a valid json. No preamble.
     2. The json should have three fields: line_count, language, tags.
     3. tags is an array of text tags. extract maximum 2 relevant tags.
     4. Language should be english or Hinglish(Hinglish means english mixed with hindi).
     
     here is the post which you need to extract metadata from:
     {post}'''
    
    pt= PromptTemplate.from_template(template)
    chain= pt | llm
    response= chain.invoke(input={'post': post}) 

    try:
        json_parser= JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Failed to parse LLM output to JSON")

    return res  
    
if __name__ == "__main__":
    process_posts("data/raw_posts.json","data/processed_posts.json")
