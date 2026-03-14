from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

print("api key loaded sucessfully",api_key[0:20])

from langchain_openai import OpenAI

llm=OpenAI(model="gpt-3.5-turbo-instruct")

result=llm.invoke("what is capital of france")

print(result)



