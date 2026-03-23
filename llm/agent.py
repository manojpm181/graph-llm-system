from llm.sql_generator import generate_sql
from utils.sql import run_sql

def agent_answer(question, schema):

    sql_query = generate_sql(question, schema)

    result = run_sql(sql_query)

    return {
        "sql": sql_query,
        "result": result
    }