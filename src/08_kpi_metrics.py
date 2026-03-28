import pandas as pd

# -------------------------
# 1 Load datasets
# -------------------------

sales = pd.read_csv("data/processed/sales_cleaned.csv")
customers = pd.read_csv("data/processed/customers_cleaned.csv")

# -------------------------
# 2 BASIC BUSINESS KPIs
# -------------------------

total_revenue = sales["Total_Amount"].sum()
total_orders = sales["Transaction_ID"].nunique()
avg_order_value = sales["Total_Amount"].mean()

total_customers = customers["Customer_ID"].nunique()

orders_per_customer = total_orders / total_customers

print("\n===== BASIC BUSINESS KPIs =====\n")

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)

print("\n===== CUSTOMER KPIs =====\n")

print("Total Customers:", total_customers)
print("Orders per Customer:", orders_per_customer)

# -------------------------
# 3 FEATURE ENGINEERING
# -------------------------

# Average price per product
sales["Avg_Price_Per_Product"] = sales["Total_Amount"] / sales["Total_Purchases"]

# High value order flag
sales["High_Value_Order"] = sales["Total_Amount"] > 2000

# Order size category
sales["Order_Size"] = pd.cut(
    sales["Total_Amount"],
    bins=[0, 500, 1500, 5000],
    labels=["Low", "Medium", "High"]
)

# -------------------------
# 4 REVENUE ANALYSIS
# -------------------------

revenue_by_category = sales.groupby("Product_Category")["Total_Amount"].sum()

print("\n===== REVENUE BY CATEGORY =====\n")
print(revenue_by_category)

revenue_by_payment = sales.groupby("Payment_Method")["Total_Amount"].sum()

print("\n===== REVENUE BY PAYMENT METHOD =====\n")
print(revenue_by_payment)

revenue_by_shipping = sales.groupby("Shipping_Method")["Total_Amount"].sum()

print("\n===== REVENUE BY SHIPPING METHOD =====\n")
print(revenue_by_shipping)

# -------------------------
# 5 MONTHLY REVENUE TREND
# -------------------------

monthly_revenue = sales.groupby("Month")["Total_Amount"].sum()

print("\n===== MONTHLY REVENUE =====\n")
print(monthly_revenue)

# -------------------------
# 6 CUSTOMER ANALYTICS
# -------------------------

# Customer Lifetime Value
customer_lifetime_value = sales.groupby("Customer_ID")["Total_Amount"].sum()

print("\n===== CUSTOMER LIFETIME VALUE =====\n")
print(customer_lifetime_value.head())

# Purchase frequency
purchase_frequency = sales.groupby("Customer_ID")["Transaction_ID"].count()

print("\n===== CUSTOMER PURCHASE FREQUENCY =====\n")
print(purchase_frequency.head())

# Revenue per customer
revenue_per_customer = sales.groupby("Customer_ID")["Total_Amount"].mean()

print("\n===== REVENUE PER CUSTOMER =====\n")
print(revenue_per_customer.head())

# -------------------------
# 7 TOP CUSTOMERS
# -------------------------

top_customers = sales.groupby("Customer_ID")["Total_Amount"].sum() \
                     .sort_values(ascending=False) \
                     .head(10)

print("\n===== TOP 10 CUSTOMERS BY REVENUE =====\n")
print(top_customers)

# -------------------------
# 8 REVENUE CONTRIBUTION %
# -------------------------

category_revenue = sales.groupby("Product_Category")["Total_Amount"].sum()

revenue_percent = (category_revenue / category_revenue.sum()) * 100

print("\n===== CATEGORY REVENUE CONTRIBUTION (%) =====\n")
print(revenue_percent)

# -------------------------
# 9 SAVE FEATURE DATASET
# -------------------------

sales.to_csv("data/processed/sales_kpi_features.csv", index=False)

print("\nKPI feature dataset created successfully")