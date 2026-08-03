import pandas as pd 

file_path = "data/Online Retail.xlsx"

df = pd.read_excel(file_path)

print(df.head())

print("\nDataSet Info:")
print(df.info())

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())