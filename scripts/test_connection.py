import os
from pathlib import Path
import psycopg2
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

print("Password loaded:", bool(os.getenv("POSTGRES_PASSWORD")))

conn = psycopg2.connect(
    host="localhost",
    database="StorePulse",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
    port="5432"
)

print("Connected to PostgreSQL successfully!")

conn.close()