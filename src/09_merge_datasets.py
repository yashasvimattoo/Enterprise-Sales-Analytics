import pandas as pd

print("Loading datasets...")

customers = pd.read_csv("data/processed/customers_cleaned.csv")
products = pd.read_csv("data/processed/products_cleaned.csv")
sales = pd.read_csv("data/processed/sales_kpi_features.csv")

# -------------------------
# FIX 1: remove duplicate product categories
# -------------------------
products = products.drop_duplicates(subset="Product_Category")

# -------------------------
# Merge 1: Sales + Customers
# -------------------------
print("Merging sales with customers...")

data = sales.merge(
    customers,
    on="Customer_ID",
    how="left"
)

print("Shape after customer merge:", data.shape)

# -------------------------
# Merge 2: Add product info
# -------------------------
print("Merging products...")

data = data.merge(
    products,
    on="Product_Category",
    how="left"
)

print("Final dataset shape:", data.shape)

# -------------------------
# Save final dataset
# -------------------------
data.to_csv(
    "data/final/final_analytics_dataset.csv",
    index=False
)

print("Final analytics dataset created successfully")