from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

print("api key loaded sucessfully",api_key[0:20])

from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-4o-mini", 
               temperature=0.1,
               max_completion_tokens=50)

result=llm.invoke("provide me report on climate change")

print(result.content)
print(result.response_metadata["token_usage"]["total_tokens"])