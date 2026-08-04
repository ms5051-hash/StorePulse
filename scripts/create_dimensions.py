import pandas as pd 

df = pd.read_csv("data/clean_sales.csv")

customer_df = df[["CustomerID", "Country"]]
customer_df = customer_df.drop_duplicates()
customer_df = customer_df.reset_index(drop=True)
customer_df.to_csv("data/dim_customer.csv", index=False)
print("Customer dimension created")

#dimension product

product_df = df[["StockCode", "Description"]]
product_df = product_df.drop_duplicates()
product_df = product_df.reset_index(drop=True)
product_df.to_csv("data/dim_product.csv", index=False)
print("Product dimension created")