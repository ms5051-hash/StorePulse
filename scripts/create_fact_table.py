import pandas as pd 

df = pd.read_csv("data/clean_sales.csv")

#Create a df that only has the important information of a transaction
fact_sales_df = df[
    [
        "InvoiceNo",
        "CustomerID",
        "StockCode",
        "InvoiceDate",
        "Quantity",
        "UnitPrice"
    ]
]

print(fact_sales_df.head())