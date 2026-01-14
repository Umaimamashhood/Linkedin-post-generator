# Linkedin-post-generator
AI-powered LinkedIn post generator using few-shot learning and LLMs

🚀 LinkedIn Post Generator (Few-Shot + LLM)

This project is an AI-powered LinkedIn Post Generator built using Python, Streamlit, LangChain, and LLMs.

The application generates LinkedIn posts by:

Analyzing previously written LinkedIn posts

Extracting tags, language, and post length

Using few-shot learning to guide the LLM

Generating new posts based on user-selected tags, language, and length

🧠 Core Idea

Instead of generating posts blindly, this project uses few-shot prompting:

Previously processed LinkedIn posts are used as examples to guide the LLM in generating more relevant, structured, and human-like content.

✨ Features

🏷 Tag-based post generation

🌐 Language selection (English / Hinglish)

📏 Length control (Short, Medium, Long)

🧠 Few-shot learning using real LinkedIn posts

🤖 LLM-powered content generation

🖥 Interactive Streamlit UI

🧩 Detailed Workflow
1️⃣ Data Preprocessing (preprocess.py)

Raw LinkedIn posts are processed to enrich them with metadata.

Steps:

Load raw LinkedIn posts from raw_posts.json

Use LLM to extract:

Line count

Language (English / Hinglish)

Relevant tags (max 2)

Normalize and unify similar tags using AI

Save cleaned data to processed_posts.json

This processed dataset becomes the knowledge base for few-shot learning.

2️⃣ Few-Shot Post Selection (few_shot.py)

Loads processed posts into a Pandas DataFrame

Categorizes posts by length:

Short

Medium

Long

Filters example posts based on:

Selected tag

Selected language

Selected length

Supplies relevant examples to the prompt

3️⃣ Prompt Construction & Generation (post_generator.py)

Builds a dynamic prompt using:

User-selected tag(s)

Language

Length

Few-shot examples

Enforces strict formatting rules:

No inverted commas

No preamble text

Sends prompt to the LLM

Returns LinkedIn-ready content

4️⃣ User Interface (main.py)

Built using Streamlit

Allows users to:

Select one or more tags

Choose language

Choose post length

Displays generated LinkedIn post instantly

5️⃣ LLM Configuration (llm_helper.py)

Uses Groq LLM (LLaMA 3.1 – 8B Instant)

API key managed securely using environment variables

Integrated via LangChain

🛠 Tech Stack

Python

Streamlit

LangChain

Groq LLM (LLaMA 3.1)

Pandas

Prompt Engineering

Few-Shot Learning

📂 Project Structure
├── main.py
├── post_generator.py
├── preprocess.py
├── few_shot.py
├── llm_helper.py
├── data/
│   ├── raw_posts.json
│   └── processed_posts.json

▶️ Running the Project
Install dependencies
pip install -r requirements.txt

Run Streamlit app
streamlit run main.py

🎯 Use Cases

LinkedIn content generation

Personal branding assistance

AI-assisted writing workflows

Learning few-shot prompting with LLMs

🔮 Future Enhancements

Tone selection (Professional / Casual / Storytelling)

Hashtag weighting & ranking

Post editing & preview

Dataset expansion for stronger few-shot results
