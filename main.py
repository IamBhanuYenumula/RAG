from dotenv import load_dotenv
from importlib.metadata import version
load_dotenv()

from langchain_ollama import ChatOllama
core_version = version("langchain-core")
lg_version = version("langgraph")

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")

def main():
    print("Hello from RAG")

    #testing qwen
    llm = ChatOllama(model="qwen3:8b", num_predict=256, reasoning=False)
    response = llm.invoke("set complete!")
    print(f"Response from chatQwen:{response}")

    print("done setup")
if __name__ == "__main__":
    main()