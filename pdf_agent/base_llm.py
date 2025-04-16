import os
from langchain_ollama import OllamaLLM


LLAMA_BASE_MODEL = "gemma3:latest"
EMBEDDING_MODEL = "nomic-embed-text:latest"

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = "Your Langsmith API Key"
os.environ["LANGSMITH_PROJECT"] = "Project Name on langsmith"

# print(os.environ)

LOCAL_LLM_INSTANCE = OllamaLLM(model=LLAMA_BASE_MODEL)