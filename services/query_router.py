def route_query(query):
    query = query.lower()

    if any(word in query for word in ["highest", "most", "count", "top", "frequent", "how many", "total"]):
        return "sql"

    if any(word in query for word in ["trace", "flow", "relationship"]):
        return "graph"

    return "sql"