import pandas as pd
import numpy as np

products = pd.read_csv("data/processed/products.csv")


products = products.drop_duplicates()


products = products.replace(r'^\s*$', np.nan, regex=True)

products = products.rename(columns={"products": "Product_Name"})

products["Product_Category"] = products["Product_Category"].fillna("Unknown")
products["Product_Brand"] = products["Product_Brand"].fillna("Unknown")
products["Product_Type"] = products["Product_Type"].fillna("Unknown")
products["Product_Name"] = products["Product_Name"].fillna("Unknown Product")

products["Product_Category"] = products["Product_Category"].str.strip().str.title()
products["Product_Brand"] = products["Product_Brand"].str.strip().str.title()
products["Product_Type"] = products["Product_Type"].str.strip().str.title()
products["Product_Name"] = products["Product_Name"].str.strip().str.title()

products["Product_Name"] = products["Product_Name"].str.replace(r"\s+", " ", regex=True)


# Product_ID 

products = products.reset_index(drop=True)
products["Product_ID"] = products.index + 1


print("Unique Categories:", products["Product_Category"].nunique())
print("Unique Brands:", products["Product_Brand"].nunique())

print("Missing values after cleaning:")
print(products.isnull().sum())

print("Dataset shape:", products.shape)

products.to_csv("data/processed/products_cleaned.csv", index=False)

print("Products dataset cleaned successfully")