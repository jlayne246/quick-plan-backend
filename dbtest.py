import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
conn_str = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(conn_str)
    print("✅ Connection works!")
    conn.close()
except Exception as e:
    print("❌ Failed:", e)
