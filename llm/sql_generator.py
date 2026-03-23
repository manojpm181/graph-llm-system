from groq import Groq
import os
import re
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def clean_sql(sql: str) -> str:
   
    sql = sql.replace("```sql", "").replace("```", "").strip()

   
    sql = sql.replace("product", "material")
    sql = sql.replace("customer", "soldtoparty")
    sql = sql.replace("order_id", "salesorder")

   
    match = re.search(r"(SELECT .*;?)", sql, re.IGNORECASE | re.DOTALL)
    if match:
        sql = match.group(1)

    return sql.strip()


def generate_sql(question: str, schema: str = "") -> str:

    prompt = f"""
You are an expert SQL generator for SQLite.

Database schema:
orders(salesorder, soldtoparty, material)

Column Mapping:
- product = material
- customer = soldtoparty
- order = salesorder

STRICT RULES:
- Use ONLY these columns: salesorder, soldtoparty, material
- NEVER use columns like product, customer, order_id
- Always use table name: orders
- Always generate VALID SQLite SQL
- Use GROUP BY when needed
- Use ORDER BY ... DESC for "top", "most", "highest"
- Use LIMIT 1 for single result questions
- Return ONLY SQL (no explanation, no markdown)
- If user asks "top N", use LIMIT N

Examples:

Q: Which product appears most frequently?
A:
SELECT material, COUNT(*) as freq
FROM orders
GROUP BY material
ORDER BY freq DESC
LIMIT 1;

Q: Total number of orders?
A:
SELECT COUNT(*) as total_orders FROM orders;

Now generate SQL.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )

    raw_sql = response.choices[0].message.content.strip()

    return clean_sql(raw_sql)