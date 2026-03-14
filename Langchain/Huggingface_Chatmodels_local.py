
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm_obj=HuggingFacePipeline.from_model_id(
    model_id="cometadata/funding-parsing-lora-Llama_3.1_8B-ep1-r64-a128-synthetic",
    task="text_generation"
)

llm1=ChatHuggingFace(llm=llm_obj)

query="what is the capital of china?"
result=llm1.invoke(query)

print(result)