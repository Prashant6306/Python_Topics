from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm_obj=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",
                        task="text_generation" , 
                        )

llm1=ChatHuggingFace(llm=llm_obj,)

query="what is the capital of china?"
result=llm1.invoke(query)

print(result)