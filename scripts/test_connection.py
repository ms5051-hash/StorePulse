import os
from pathlib import Path
import psycopg2
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

conn = psycopg2.connect(
    host="localhost",
    database="storepulse",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
    port="5432"
)

print("Connected to PostgreSQL successfully!")

conn.close()