def build_prompt(query):
    return f"""
You are analyzing SAP Order-to-Cash data.

Answer ONLY based on dataset.

User Question:
{query}
"""