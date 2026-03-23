from utils.loader import load_data
import sqlite3

df = load_data()

conn = sqlite3.connect("db/database.db")
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Database created")