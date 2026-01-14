from llm_helper import llm
from few_shot import FewShotPosts

few_shot= FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "5 to 7 lines"
    elif length == "Medium":
        return "8 to 10 lines"
    else:
        return "more than 10 lines"

def get_prompt(length, language, tag):
    length_str = get_length_str(length)
    prompt = f"""
        1)Generate a LinkedIn post in {language} language with a length of {length_str} on the topic of {tag}. 
        2)No Permeable. No inverted commas. Dont write here is the post.
        3)If language is Hinglish then use mix of Hindi language and English language. Not complete Hindi
        """
    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) >0:
        prompt += " 4) Here are some examples to help you generate the post:\n"
        for i,post in enumerate(examples):
            post_text= post['text']
            prompt += f"\n\nExample {i+1}\n\n {post_text}"
            if i == 1:
                break
    return prompt

def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)

    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    post = generate_post(length="Short", language="Hinglish", tag="Job")
    print(post)
