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
# 3 Rename column (CRITICAL FIX)
# -------------------------
products = products.rename(columns={"products": "Product_Name"})

# -------------------------
# 4 Fill missing values
# -------------------------
products["Product_Category"] = products["Product_Category"].fillna("Unknown")
products["Product_Brand"] = products["Product_Brand"].fillna("Unknown")
products["Product_Type"] = products["Product_Type"].fillna("Unknown")
products["Product_Name"] = products["Product_Name"].fillna("Unknown Product")

# -------------------------
# 5 Standardize text formatting
# -------------------------
products["Product_Category"] = products["Product_Category"].str.strip().str.title()
products["Product_Brand"] = products["Product_Brand"].str.strip().str.title()
products["Product_Type"] = products["Product_Type"].str.strip().str.title()
products["Product_Name"] = products["Product_Name"].str.strip().str.title()

# -------------------------
# 6 Remove weird spacing
# -------------------------
products["Product_Name"] = products["Product_Name"].str.replace(r"\s+", " ", regex=True)

# -------------------------
# 7 Create Product_ID (MOST IMPORTANT FIX 🔥)
# -------------------------
products = products.reset_index(drop=True)
products["Product_ID"] = products.index + 1

# -------------------------
# 8 Data validation
# -------------------------
print("Unique Categories:", products["Product_Category"].nunique())
print("Unique Brands:", products["Product_Brand"].nunique())

# -------------------------
# 9 Final quality check
# -------------------------
print("Missing values after cleaning:")
print(products.isnull().sum())

print("Dataset shape:", products.shape)

# save cleaned dataset
products.to_csv("data/processed/products_cleaned.csv", index=False)

print("Products dataset cleaned successfully")