import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import os

# Grabs the .env file 
env_file = Path(__file__).resolve().parent.parent / ".env"  
load_dotenv(env_file)

password = os.getenv("POSTGRES_PASSWORD")

#Creating the connection to PostreSQL
engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/storepulse"
)

data_folder = Path(__file__).resolve().parent.parent / "data"

df_customer = pd.read_csv(data_folder / "dim_customer.csv")
df_date = pd.read_csv(data_folder / "dim_date.csv")
df_product = pd.read_csv(data_folder / "dim_product.csv")
df_sales = pd.read_csv(data_folder / "fact_sales.csv")

df_customer.to_sql("dim_customer", engine, if_exists="replace", index=False)
df_date.to_sql("dim_date", engine, if_exists="replace", index=False)
df_product.to_sql("dim_product", engine, if_exists="replace", index=False)
df_sales.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("Data loaded into PostreSQL successfully!")

engine.dispose()
