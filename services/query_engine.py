from llm.agent import agent_answer
from llm.prompt import build_prompt
from llm.llm_engine import ask_llm
from services.query_router import route_query

def process_query(user_input):

    route = route_query(user_input)

    if route == "sql":
        schema = "orders(salesorder, soldtoparty, material)"
        response = agent_answer(user_input, schema)

        return {
            "type": "sql",
            "data": response
        }

    elif route == "graph":
        return {
            "type": "graph",
            "data": "Graph view"
        }

    else:
        prompt = build_prompt(user_input)
        response = ask_llm(prompt)

        return {
            "type": "llm",
            "data": response
        }