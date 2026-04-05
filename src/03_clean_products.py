import pandas as pd
import numpy as np

products = pd.read_csv("data/processed/products.csv")

# -------------------------
# 1 Remove duplicate rows
# -------------------------
products = products.drop_duplicates()

# -------------------------
# 2 Replace blank strings with NaN
# -------------------------
products = products.replace(r'^\s*$', np.nan, regex=True)

# -------------------------
# 3 Fill missing values
# -------------------------
products["Product_Category"] = products["Product_Category"].fillna("Unknown")
products["Product_Brand"] = products["Product_Brand"].fillna("Unknown")

# -------------------------
# 4 Standardize text formatting
# -------------------------
products["Product_Category"] = products["Product_Category"].str.strip().str.title()
products["Product_Brand"] = products["Product_Brand"].str.strip().str.title()
products["Product_Type"] = products["Product_Type"].str.strip().str.title()
products["products"] = products["products"].str.strip().str.title()

# -------------------------
# 5 Remove weird spacing
# -------------------------
products["products"] = products["products"].str.replace(r"\s+", " ", regex=True)

# -------------------------
# 6 Data validation
# -------------------------
print("Unique Categories:", products["Product_Category"].nunique())
print("Unique Brands:", products["Product_Brand"].nunique())

# -------------------------
# 7 Final quality check
# -------------------------
print("Missing values after cleaning:")
print(products.isnull().sum())

print("Dataset shape:", products.shape)

# save cleaned dataset
products.to_csv("data/processed/products_cleaned.csv", index=False)

print("Products dataset cleaned successfully")