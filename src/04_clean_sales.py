import pandas as pd

sales = pd.read_csv("data/processed/sales.csv")


sales = sales.drop_duplicates(
    subset=["Transaction_ID", "Product_Name", "Product_Category", "Product_Brand"]
)

sales = sales.replace(r'^\s*$', None, regex=True)


sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce", format="mixed")

sales["Amount"] = pd.to_numeric(sales["Amount"], errors="coerce")
sales["Total_Amount"] = pd.to_numeric(sales["Total_Amount"], errors="coerce")
sales["Total_Purchases"] = pd.to_numeric(sales["Total_Purchases"], errors="coerce")
sales["Ratings"] = pd.to_numeric(sales["Ratings"], errors="coerce")

sales = sales[sales["Amount"] > 0]
sales = sales[sales["Total_Amount"] > 0]


sales["Ratings"] = sales["Ratings"].fillna(sales["Ratings"].median())
sales["Feedback"] = sales["Feedback"].fillna("No Feedback")

sales["Product_Brand"] = sales["Product_Brand"].fillna("Unknown")
sales["Shipping_Method"] = sales["Shipping_Method"].fillna("Unknown")
sales["Payment_Method"] = sales["Payment_Method"].fillna("Unknown")
sales["Order_Status"] = sales["Order_Status"].fillna("Unknown")
sales["Product_Category"] = sales["Product_Category"].fillna("Unknown")
sales["Product_Name"] = sales["Product_Name"].fillna("Unknown Product")


sales["Product_Name"] = sales["Product_Name"].str.strip().str.title()
sales["Product_Category"] = sales["Product_Category"].str.strip().str.title()
sales["Product_Brand"] = sales["Product_Brand"].str.strip().str.title()
sales["Payment_Method"] = sales["Payment_Method"].str.strip().str.title()
sales["Shipping_Method"] = sales["Shipping_Method"].str.strip().str.title()
sales["Order_Status"] = sales["Order_Status"].str.strip().str.title()

# Map Product_ID
products = pd.read_csv("data/processed/products_cleaned.csv")

products["Product_Name"] = products["Product_Name"].str.strip().str.title()
products["Product_Category"] = products["Product_Category"].str.strip().str.title()
products["Product_Brand"] = products["Product_Brand"].fillna("Unknown").str.strip().str.title()

sales = sales.merge(
    products[["Product_ID", "Product_Name", "Product_Category", "Product_Brand"]],
    on=["Product_Name", "Product_Category", "Product_Brand"],
    how="left"
)

# Remove rows missing critical fields
sales = sales.dropna(subset=["Transaction_ID", "Customer_ID", "Date"])


sales["Total_Purchases"] = sales["Total_Purchases"].fillna(
    sales["Total_Purchases"].median()
)

# Remove extreme revenue outliers using IQR
Q1 = sales["Total_Amount"].quantile(0.25)
Q3 = sales["Total_Amount"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

sales = sales[
    (sales["Total_Amount"] >= lower_limit) &
    (sales["Total_Amount"] <= upper_limit)
]


sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month
sales["Time"] = sales["Time"].fillna("Unknown")

print("Missing values after cleaning:")
print(sales.isnull().sum())

print("Dataset shape:", sales.shape)
print("Missing Product_ID:", sales["Product_ID"].isnull().sum())

sales.to_csv("data/processed/sales_cleaned.csv", index=False)

print("Sales dataset cleaned successfully")