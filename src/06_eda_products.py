import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# 1 Load cleaned dataset
# -------------------------
products = pd.read_csv("data/processed/products_cleaned.csv")

print("Dataset shape:", products.shape)
print("\nColumns:\n", products.columns)

# -------------------------
# 2 Dataset info
# -------------------------
print("\nDataset Info:\n")
print(products.info())

# -------------------------
# 3 Missing values check
# -------------------------
print("\nMissing values:\n")
print(products.isnull().sum())

# -------------------------
# 4 Product category distribution
# -------------------------
print("\nProduct categories:\n")
print(products["Product_Category"].value_counts())

plt.figure()
products["Product_Category"].value_counts().plot(kind="bar")
plt.title("Product Category Distribution")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig("reports/figures/product_category_distribution.png")
plt.close()

# -------------------------
# 5 Product brand distribution
# -------------------------
print("\nTop brands:\n")
print(products["Product_Brand"].value_counts().head(10))

plt.figure()
products["Product_Brand"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Product Brands")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig("reports/figures/top_product_brands.png")
plt.close()

# -------------------------
# 6 Product type distribution
# -------------------------
print("\nProduct types:\n")
print(products["Product_Type"].value_counts().head(10))

plt.figure()
products["Product_Type"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Product Types")
plt.xlabel("Product Type")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig("reports/figures/top_product_types.png")
plt.close()