def validate_query(query):
    allowed = ["order", "customer", "product"]

    return any(word in query.lower() for word in allowed)