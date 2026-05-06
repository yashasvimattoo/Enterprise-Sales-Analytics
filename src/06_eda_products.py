import pandas as pd
import matplotlib.pyplot as plt

products = pd.read_csv("data/processed/products_cleaned.csv")

print("Dataset shape:", products.shape)
print("\nColumns:\n", products.columns)


print("\nDataset Info:\n")
print(products.info())


print("\nMissing values:\n")
print(products.isnull().sum())


#  Product category distribution

print("\nProduct categories:\n")
print(products["Product_Category"].value_counts())
print("Top Category:", products["Product_Category"].value_counts().idxmax())

plt.figure()
products["Product_Category"].value_counts().plot(kind="bar")
plt.title("Product Category Distribution")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig("reports/figures/product_category_distribution.png")
plt.close()

#  Product brand distribution

print("\nTop brands:\n")
print(products["Product_Brand"].value_counts().head(10))
print("Top Brand:", products["Product_Brand"].value_counts().idxmax())

plt.figure()
products["Product_Brand"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Product Brands")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig("reports/figures/top_product_brands.png")
plt.close()


#  Product type distribution

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