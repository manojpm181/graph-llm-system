import sqlite3
import hashlib

DB_PATH = "db/database.db"


def connect():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def create_users_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, email, password):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hash_password(password))
        )
        conn.commit()
        return True

    except Exception as e:
        print("🔥 REGISTER ERROR:", e)   # VERY IMPORTANT
        return False

    finally:
        conn.close()


def login_user(email, password):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )

    user = cursor.fetchone()
    conn.close()

    return user