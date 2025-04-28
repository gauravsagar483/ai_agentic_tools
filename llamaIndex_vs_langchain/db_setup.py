from langchain_community.utilities import SQLDatabase as LangChainSQLDatabase
from llama_index.core import SQLDatabase as LLmaIndexSQLDatabase

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
    insert,
    text,
)

from sqlalchemy.pool import StaticPool



engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

metadata_obj = MetaData()


table_name = "city_stats"
city_stats_table = Table(
    table_name,
    metadata_obj,
    Column("city_name", String(16), primary_key=True),
    Column("population", Integer),
    Column("country", String(16), nullable=False),
)
metadata_obj.create_all(engine)


rows = [
    {"city_name": "Toronto", "population": 2930000, "country": "Canada"},
    {"city_name": "Tokyo", "population": 13960000, "country": "Japan"},
    {
        "city_name": "Chicago",
        "population": 2679000,
        "country": "United States",
    },
    {"city_name": "Seoul", "population": 9776000, "country": "South Korea"},
]
for row in rows:
    stmt = insert(city_stats_table).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)


print("\nDB Initialized !!\n")


langchain_db = LangChainSQLDatabase(engine, include_tables=["city_stats"])
llamaindex_db = LLmaIndexSQLDatabase(engine, include_tables=["city_stats"])


# view current table
stmt = select(
    city_stats_table.c.city_name,
    city_stats_table.c.population,
    city_stats_table.c.country,
).select_from(city_stats_table)

with engine.connect() as connection:
    results = connection.execute(stmt).fetchall()
    print("\n".join(str(result) for result in results))

print("\nCities:\n")

with engine.connect() as con:
    rows = con.execute(text("SELECT city_name from city_stats"))
    for row in rows:
        print(row[0])
