from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")

print("api key loaded sucessfully",api_key[0:20])

from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-3.1-pro-preview")

query="what is the capitalof china?"

result=llm.invoke(query)

print(result)