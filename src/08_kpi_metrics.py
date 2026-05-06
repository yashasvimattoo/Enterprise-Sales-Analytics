import pandas as pd


sales = pd.read_csv("data/processed/sales_cleaned.csv")
customers = pd.read_csv("data/processed/customers_cleaned.csv")


total_revenue = sales["Total_Amount"].sum()
total_orders = sales["Transaction_ID"].nunique()
avg_order_value = sales["Total_Amount"].mean()

total_customers = customers["Customer_ID"].nunique()

orders_per_customer = total_orders / total_customers

print("BASIC BUSINESS KPIs ")

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)

print("CUSTOMER KPIs")

print("Total Customers:", total_customers)
print("Orders per Customer:", orders_per_customer)


# FEATURE ENGINEERING

# Average price per product
sales["Avg_Price_Per_Product"] = sales["Total_Amount"] / sales["Total_Purchases"].replace(0,1)

# High value order flag
sales["High_Value_Order"] = sales["Total_Amount"] > 2000

# Order size category
sales["Order_Size"] = pd.cut(
    sales["Total_Amount"],
    bins=[0, 500, 1500, 5000],
    labels=["Low", "Medium", "High"]
)


# 4 REVENUE ANALYSIS

revenue_by_category = sales.groupby("Product_Category")["Total_Amount"].sum()

print("REVENUE BY CATEGORY")
print(revenue_by_category)
print("Top Revenue Category:", revenue_by_category.idxmax())

revenue_by_payment = sales.groupby("Payment_Method")["Total_Amount"].sum()

print("REVENUE BY PAYMENT METHOD")
print(revenue_by_payment)
print("Top Payment Revenue:", revenue_by_payment.idxmax())

revenue_by_shipping = sales.groupby("Shipping_Method")["Total_Amount"].sum()

print("REVENUE BY SHIPPING METHOD")
print(revenue_by_shipping)
print("Top Shipping Revenue:", revenue_by_shipping.idxmax())


# 5 MONTHLY REVENUE TREND

monthly_revenue = sales.groupby("Month")["Total_Amount"].sum()

print(" MONTHLY REVENUE")
print(monthly_revenue)
print("Peak Revenue Month:", monthly_revenue.idxmax())


#  CUSTOMER ANALYTICS

# Customer Lifetime Value
customer_lifetime_value = sales.groupby("Customer_ID")["Total_Amount"].sum()

print("CUSTOMER LIFETIME VALUE")
print(customer_lifetime_value.head())
print("Top Customer CLV:", customer_lifetime_value.max())

# Purchase frequency
purchase_frequency = sales.groupby("Customer_ID")["Transaction_ID"].count()

print("CUSTOMER PURCHASE FREQUENCY")
print(purchase_frequency.head())

# Revenue per customer
revenue_per_customer = sales.groupby("Customer_ID")["Total_Amount"].mean()

print(" REVENUE PER CUSTOMER")
print(revenue_per_customer.head())


#  TOP CUSTOMERS
top_customers = sales.groupby("Customer_ID")["Total_Amount"].sum() \
                     .sort_values(ascending=False) \
                     .head(10)

print("TOP 10 CUSTOMERS BY REVENUE")
print(top_customers)


#  REVENUE CONTRIBUTION 

category_revenue = sales.groupby("Product_Category")["Total_Amount"].sum()

revenue_percent = (category_revenue / category_revenue.sum()) * 100

print("CATEGORY REVENUE CONTRIBUTION")
print(revenue_percent)
print("Highest Contribution Category:", revenue_percent.idxmax())



sales.to_csv("data/processed/sales_kpi_features.csv", index=False)

print("KPI feature dataset created successfully")