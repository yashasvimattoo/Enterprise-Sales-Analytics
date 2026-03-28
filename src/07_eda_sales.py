import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# 1 Load cleaned dataset
# -------------------------
sales = pd.read_csv("data/processed/sales_cleaned.csv")

print("Dataset shape:", sales.shape)
print("\nColumns:\n", sales.columns)

# -------------------------
# 2 Dataset info
# -------------------------
print("\nDataset Info:\n")
print(sales.info())

# -------------------------
# 3 Missing values
# -------------------------
print("\nMissing values:\n")
print(sales.isnull().sum())

# -------------------------
# 4 Revenue statistics
# -------------------------
print("\nRevenue statistics:\n")
print(sales["Total_Amount"].describe())

plt.figure()
sales["Total_Amount"].plot(kind="hist", bins=30)

plt.title("Revenue Distribution")
plt.xlabel("Order Revenue")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("reports/figures/revenue_distribution.png")
plt.close()

# -------------------------
# 5 Payment method distribution
# -------------------------
print("\nPayment methods:\n")
print(sales["Payment_Method"].value_counts())

plt.figure()
sales["Payment_Method"].value_counts().plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("reports/figures/payment_method_distribution.png")
plt.close()

# -------------------------
# 6 Shipping methods
# -------------------------
print("\nShipping methods:\n")
print(sales["Shipping_Method"].value_counts())

plt.figure()
sales["Shipping_Method"].value_counts().plot(kind="bar")

plt.title("Shipping Method Distribution")
plt.xlabel("Shipping Method")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("reports/figures/shipping_method_distribution.png")
plt.close()

# -------------------------
# 7 Order status
# -------------------------
print("\nOrder status:\n")
print(sales["Order_Status"].value_counts())

# -------------------------
# 8 Ratings distribution
# -------------------------
print("\nRatings distribution:\n")
print(sales["Ratings"].value_counts())

plt.figure()
sales["Ratings"].value_counts().sort_index().plot(kind="bar")

plt.title("Customer Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("reports/figures/ratings_distribution.png")
plt.close()

# -------------------------
# 9 Product category sales
# -------------------------
print("\nSales by product category:\n")
print(sales["Product_Category"].value_counts())

# -------------------------
# 10 Monthly sales trend
# -------------------------
print("\nMonthly sales trend:\n")
print(sales.groupby("Month")["Total_Amount"].sum().sort_index())

monthly_sales = sales.groupby("Month")["Total_Amount"].sum().sort_index()

plt.figure()
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("reports/figures/monthly_revenue_trend.png")
plt.close()