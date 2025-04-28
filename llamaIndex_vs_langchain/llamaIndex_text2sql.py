from db_setup import llamaindex_db as sql_database

from llama_index.core.retrievers import NLSQLRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.ollama import Ollama


llm = Ollama(model="gemma3:latest", request_timeout=120.0)
embed_str_model = "nomic-embed-text:latest"


nl_sql_retriever = NLSQLRetriever(
    sql_database,
    tables=["city_stats"],
    return_raw=False,
    llm=llm,
    embed_model=embed_str_model,
)


query_engine = RetrieverQueryEngine.from_args(
    nl_sql_retriever, llm=llm, embed_model=embed_str_model
)


query = "Return the top 3 cities (along with their populations) with the highest population."
response = query_engine.query(query)

print(f"\n{query}\n" + str(response) + "\n")
