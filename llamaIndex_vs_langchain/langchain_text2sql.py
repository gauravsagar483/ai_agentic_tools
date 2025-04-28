from db_setup import langchain_db as db
from common.base_llm import chat_llm as llm

from typing_extensions import Annotated, TypedDict
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool

from langchain import hub

query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")


class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str


class QueryOutput(TypedDict):
    """Generated SQL query."""

    query: Annotated[str, ..., "Syntactically valid SQL query."]


def prepate_sql_query(state: State):
    """Generate SQL query to fetch information."""
    prompt = query_prompt_template.invoke(
        {
            "dialect": db.dialect,
            "top_k": 10,
            "table_info": db.get_table_info(),
            "input": state["question"],
        }
    )
    structured_llm = llm.with_structured_output(QueryOutput)
    result = structured_llm.invoke(prompt)
    return {"query": result["query"]}


query = "Return the top 3 cities (along with their populations) with the highest population."

print(f"\n{query}\n")
sql = prepate_sql_query({"question": query})
print(sql)


def execute_query(state: State):
    """Execute SQL query."""
    execute_query_tool = QuerySQLDatabaseTool(db=db)
    return {"result": execute_query_tool.invoke(state["query"])}


print(execute_query({"query": sql}))



