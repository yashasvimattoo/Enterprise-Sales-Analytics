import pandas as pd


sales = pd.read_csv("data/processed/sales.csv")

sales = sales.drop_duplicates(subset="Transaction_ID")

sales = sales.replace(r'^\s*$', None, regex=True)

sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")

sales["Amount"] = pd.to_numeric(sales["Amount"], errors="coerce")
sales["Total_Amount"] = pd.to_numeric(sales["Total_Amount"], errors="coerce")
sales["Total_Purchases"] = pd.to_numeric(sales["Total_Purchases"], errors="coerce")
sales["Ratings"] = pd.to_numeric(sales["Ratings"], errors="coerce")

sales = sales[sales["Amount"] > 0]
sales = sales[sales["Total_Amount"] > 0]


sales["Ratings"] = sales["Ratings"].fillna(sales["Ratings"].median())

sales["Feedback"] = sales["Feedback"].fillna("No Feedback")

sales["Payment_Method"] = sales["Payment_Method"].str.strip().str.title()
sales["Shipping_Method"] = sales["Shipping_Method"].str.strip().str.title()
sales["Order_Status"] = sales["Order_Status"].str.strip().str.title()


#  Product_ID mapping

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

#  Outlier detection (IQR)

Q1 = sales["Total_Amount"].quantile(0.25)
Q3 = sales["Total_Amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

sales = sales[(sales["Total_Amount"] >= lower) & (sales["Total_Amount"] <= upper)]


sales = sales.dropna(subset=["Transaction_ID", "Customer_ID", "Date"])

sales["Shipping_Method"] = sales["Shipping_Method"].fillna("Unknown")
sales["Payment_Method"] = sales["Payment_Method"].fillna("Unknown")
sales["Order_Status"] = sales["Order_Status"].fillna("Unknown")
sales["Product_Category"] = sales["Product_Category"].fillna("Unknown")


sales["Total_Purchases"] = sales["Total_Purchases"].fillna(
    sales["Total_Purchases"].median()
)


sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month
sales["Time"] = sales["Time"].fillna("Unknown")

print("Missing values after cleaning:\n")
print(sales.isnull().sum())

print("\nDataset shape:", sales.shape)


sales.to_csv("data/processed/sales_cleaned.csv", index=False)

print("Sales dataset cleaned successfully")
print("Missing Product_ID:", sales["Product_ID"].isnull().sum())