import pandas as pd

customers = pd.read_csv("data/processed/customers_cleaned.csv")
products = pd.read_csv("data/processed/products_cleaned.csv")
sales = pd.read_csv("data/processed/sales_kpi_features.csv")


sales["Product_Name"] = sales["Product_Name"].str.strip().str.title()
sales["Product_Category"] = sales["Product_Category"].str.strip().str.title()

products["Product_Name"] = products["Product_Name"].str.strip().str.title()
products["Product_Category"] = products["Product_Category"].str.strip().str.title()


products = products.drop_duplicates(
    subset=["Product_Name", "Product_Category"]
)


data = sales.merge(
    customers,
    on="Customer_ID",
    how="left"
)

print("Shape after customer merge:", data.shape)


data = data.merge(
    products[["Product_ID", "Product_Name", "Product_Category"]],
    on=["Product_Name", "Product_Category"],
    how="left",
    suffixes=("", "_prod")
)

print("Shape after product merge:", data.shape)


if "Product_ID_prod" in data.columns:
    data["Product_ID"] = data["Product_ID_prod"].fillna(data.get("Product_ID"))
    data.drop(columns=["Product_ID_prod"], inplace=True)

missing_products = data["Product_ID"].isnull().sum()
print("Missing Product_ID after merge:", missing_products)

print("Final dataset shape:", data.shape)

data.to_csv(
    "data/final/final_analytics_dataset.csv",
    index=False
)

print("Final analytics dataset created successfully")