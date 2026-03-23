import sqlite3
from utils.loader import load_data, load_jsonl_folder

def load_into_db():

    orders = load_jsonl_folder("sales_order_headers")
    items = load_jsonl_folder("sales_order_items")

    orders.columns = orders.columns.str.lower()
    items.columns = items.columns.str.lower()

    df = orders.merge(items, on="salesorder", how="inner")

    conn = sqlite3.connect("db/database.db")

    df.to_sql("orders", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("Orders + Items merged and loaded into DB")