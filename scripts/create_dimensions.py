import pandas as pd 

df = pd.read_csv("data/clean_sales.csv")

customer_df = df[["CustomerID", "Country"]]
customer_df = customer_df.drop_duplicates()
customer_df = customer_df.reset_index(drop=True)
customer_df.insert(0, "customer_id", customer_df.index + 1)
customer_df.to_csv("data/dim_customer.csv", index=False)
print("Customer dimension created")

#dimension product

product_df = df[["StockCode", "Description"]]

product_df = product_df.drop_duplicates(
    subset=["StockCode"]
)

product_df = product_df.reset_index(drop=True)
product_df.insert(0, "product_id", product_df.index + 1)
product_df.to_csv("data/dim_product.csv", index=False)
print("Product dimension created")

date_df = df[["InvoiceDate"]]
date_df["InvoiceDate"] = pd.to_datetime(date_df["InvoiceDate"])
date_df = date_df.drop_duplicates()
date_df = date_df.reset_index(drop=True)

date_df.insert(0, "date_id", date_df.index + 1)

# Create extra date columns
date_df["Year"] = date_df["InvoiceDate"].dt.year
date_df["Month"] = date_df["InvoiceDate"].dt.month
date_df["Day"] = date_df["InvoiceDate"].dt.day
date_df["Hour"] = date_df["InvoiceDate"].dt.hour

date_df.to_csv("data/dim_date.csv", index=False)

print("Date dimension created!")
