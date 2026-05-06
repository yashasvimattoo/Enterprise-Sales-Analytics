import pandas as pd

# -------------------------
# 1 Load dataset
# -------------------------
sales = pd.read_csv("data/processed/sales.csv")

# -------------------------
# 2 Remove duplicate transactions
# -------------------------
sales = sales.drop_duplicates(subset="Transaction_ID")

# -------------------------
# 3 Replace blank strings with NaN
# -------------------------
sales = sales.replace(r'^\s*$', None, regex=True)

# -------------------------
# 4 Convert date column
# -------------------------
sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")

# -------------------------
# 5 Convert numeric columns
# -------------------------
sales["Amount"] = pd.to_numeric(sales["Amount"], errors="coerce")
sales["Total_Amount"] = pd.to_numeric(sales["Total_Amount"], errors="coerce")
sales["Total_Purchases"] = pd.to_numeric(sales["Total_Purchases"], errors="coerce")
sales["Ratings"] = pd.to_numeric(sales["Ratings"], errors="coerce")

# -------------------------
# 6 Remove invalid amounts
# -------------------------
sales = sales[sales["Amount"] > 0]
sales = sales[sales["Total_Amount"] > 0]

# -------------------------
# 7 Handle missing ratings
# -------------------------
sales["Ratings"] = sales["Ratings"].fillna(sales["Ratings"].median())

# -------------------------
# 8 Handle missing feedback
# -------------------------
sales["Feedback"] = sales["Feedback"].fillna("No Feedback")

# -------------------------
# 9 Standardize categorical text
# -------------------------
sales["Payment_Method"] = sales["Payment_Method"].str.strip().str.title()
sales["Shipping_Method"] = sales["Shipping_Method"].str.strip().str.title()
sales["Order_Status"] = sales["Order_Status"].str.strip().str.title()

# -------------------------
# 🔥 Product_ID mapping (ADD HERE)
# -------------------------
products = pd.read_csv("data/processed/products_cleaned.csv")

# standardize before merge
sales["Product_Name"] = sales["Product_Name"].str.strip().str.title()
sales["Product_Category"] = sales["Product_Category"].str.strip().str.title()

products["Product_Name"] = products["Product_Name"].str.strip().str.title()
products["Product_Category"] = products["Product_Category"].str.strip().str.title()

# merge
sales = sales.merge(
    products[["Product_ID", "Product_Name", "Product_Category"]],
    on=["Product_Name", "Product_Category"],
    how="left"
)

# -------------------------
# 10 Outlier detection (IQR)
# -------------------------
Q1 = sales["Total_Amount"].quantile(0.25)
Q3 = sales["Total_Amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

sales = sales[(sales["Total_Amount"] >= lower) & (sales["Total_Amount"] <= upper)]

# -------------------------
# 11 Remove rows with missing critical fields
# -------------------------
sales = sales.dropna(subset=["Transaction_ID", "Customer_ID", "Date"])

# -------------------------
# 12 Fill missing categorical values
# -------------------------
sales["Shipping_Method"] = sales["Shipping_Method"].fillna("Unknown")
sales["Payment_Method"] = sales["Payment_Method"].fillna("Unknown")
sales["Order_Status"] = sales["Order_Status"].fillna("Unknown")
sales["Product_Category"] = sales["Product_Category"].fillna("Unknown")

# -------------------------
# 13 Fill numeric columns
# -------------------------
sales["Total_Purchases"] = sales["Total_Purchases"].fillna(
    sales["Total_Purchases"].median()
)

# -------------------------
# 14 Regenerate year and month
# -------------------------
sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month
sales["Time"] = sales["Time"].fillna("Unknown")

# -------------------------
# 15 Final data quality check
# -------------------------
print("Missing values after cleaning:\n")
print(sales.isnull().sum())

print("\nDataset shape:", sales.shape)

# -------------------------
# 16 Save cleaned dataset
# -------------------------
sales.to_csv("data/processed/sales_cleaned.csv", index=False)

print("\nSales dataset cleaned successfully")
print("Missing Product_ID:", sales["Product_ID"].isnull().sum())