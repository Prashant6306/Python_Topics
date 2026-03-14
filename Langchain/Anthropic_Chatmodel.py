from dotenv import load_dotenv

import os

load_dotenv()
api_key=os.getenv("ANTHROPIC_API_KEY")

print("api key loaded sucessfully",api_key[0:20])

from langchain_anthropic import ChatAnthropic

llm=ChatAnthropic( model="claude-haiku-4-5-20251001",api_key=api_key)

query="what is the capitalof china?"

result=llm.invoke(query)

print(result)