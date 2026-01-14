from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
llm=ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant")

if __name__ == "__main__":
    response= llm.invoke(" What is the capital of France?")
    print(response.content)