import os
from langchain_ollama import OllamaLLM, ChatOllama
from langchain_ollama.embeddings import OllamaEmbeddings

LLAMA_BASE_MODEL = "gemma3:latest"
DEEP_SEEK_MODEL = "deepseek-r1:latest"
EMBEDDING_MODEL = "nomic-embed-text:latest"

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = "Your Langsmith API Key"
os.environ["LANGSMITH_PROJECT"] = "Project Name on langsmith"

# print(os.environ)

LOCAL_LLM_INSTANCE = OllamaLLM(model=LLAMA_BASE_MODEL)
EMBEDDING_INSTANCE = OllamaEmbeddings(model=EMBEDDING_MODEL)

chat_llm = ChatOllama(model=DEEP_SEEK_MODEL)

smollm_tools_llm = ChatOllama(model="smollm2:latest")