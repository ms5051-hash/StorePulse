import pandas as pd 

#Load the clean sales data
sales_df = pd.read_csv("data/clean_sales.csv")

#Load the clean data tables
customer_df = pd.read_csv("data/dim_customer.csv")
date_df = pd.read_csv("data/dim_date.csv")
product_df = pd.read_csv("data/dim_product.csv")

print("Files loaded succcessfully")

#Merging customer dimensions
sales_df = sales_df.merge(
    customer_df[["CustomerID", "customer_id"]],
    on="CustomerID",
    how="left"
)

# 4. Add product_id
sales_df = sales_df.merge(
    product_df[["StockCode", "product_id"]],
    on="StockCode",
    how="left"
)


# Convert InvoiceDate columns to datetime
sales_df["InvoiceDate"] = pd.to_datetime(sales_df["InvoiceDate"])
date_df["InvoiceDate"] = pd.to_datetime(date_df["InvoiceDate"])


# Merge date dimension
sales_df = sales_df.merge(
    date_df[["InvoiceDate", "date_id"]],
    on="InvoiceDate",
    how="left"
)

print("Date dimension merged!")

# Calculate total sales for each transaction
sales_df["sales_amount"] = (
    sales_df["Quantity"] * sales_df["UnitPrice"]
)


#Create a unique ID for every row in the fact table
sales_df.insert(
    0,
    "sales_id",
    range(1, len(sales_df) + 1)
)

# Creating the final table with the required columns only
fact_sales = sales_df[
    [
    "sales_id",
    "InvoiceNo",
    "customer_id",
    "product_id",
    "date_id",
    "Quantity",
    "UnitPrice",
    "sales_amount"
    ]
]

fact_sales.to_csv("data/fact_sales.csv", index=False)
print("Fact sales created")


print(sales_df.head())
print(sales_df.columns)


