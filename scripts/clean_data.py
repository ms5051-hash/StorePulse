#Will remove duplicates
#handle missing values
#convert dates property
#standarize column names
#create clean CSV ready for PostgreSQL

"""
Clean the raw retail sales dataset.

- Removes duplicate records
- Removes rows with missing CustomerID
- Converts InvoiceDate to datetime
- Removes invalid transactions
- Saves a cleaned dataset for loading into PostgreSQL
"""

import pandas as pd 

#Data frame that makes the table
df = pd.read_excel("data/Online Retail.xlsx")

print("Original Shape:", df.shape)

#Remove duplicate rows
df = df.drop_duplicates()

#Remove missing Customer IDs
df = df.dropna(subset=["CustomerID"])

#Convert InvoiceDate so can convert to year, month, day, hour, minute 
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

#Remove invalid sales
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# Save cleaned dataset
df.to_csv("data/clean_sales.csv", index=False)

print("Clean dataset saved!")
