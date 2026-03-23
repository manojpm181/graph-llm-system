import pandas as pd
import os

BASE_PATH = "data/sap-o2c-data"

def load_jsonl_folder(folder):
    path = os.path.join(BASE_PATH, folder)
    files = [f for f in os.listdir(path) if f.endswith(".jsonl")]

    df_list = []
    for file in files:
        df = pd.read_json(os.path.join(path, file), lines=True)
        df_list.append(df)

    return pd.concat(df_list, ignore_index=True)

def load_data():
    orders = load_jsonl_folder("sales_order_headers")
    items = load_jsonl_folder("sales_order_items")

    orders.columns = orders.columns.str.lower()
    items.columns = items.columns.str.lower()

    df = items.merge(orders, on="salesorder", how="left")

    return df