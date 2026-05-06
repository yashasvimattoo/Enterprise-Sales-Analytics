import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("data/processed/customers_cleaned.csv")

print("Dataset shape:", customers.shape)
print("\nColumns:\n", customers.columns)


print("\nDataset Info:\n")
print(customers.info())

print("\nAge statistics:\n")
print(customers["Age"].describe())
# AGE DISTRIBUTION CHART
plt.figure()
customers["Age"].plot(kind="hist", bins=20)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("reports/figures/age_distribution.png")
plt.close()

# Gender Distrubution
print("\nGender distribution:\n")
print(customers["Gender"].value_counts())

plt.figure()
customers["Gender"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("reports/figures/gender_distribution.png")
plt.close()

#Customer Distribution
print("\nCustomer segments:\n")
print(customers["Customer_Segment"].value_counts())

plt.figure()
customers["Customer_Segment"].value_counts().plot(kind="bar")
plt.title("Customer Segment Distribution")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("reports/figures/customer_segment_distribution.png")
plt.close()


# Income distribution

print("\nIncome levels:\n")
print(customers["Income"].value_counts())


# Top cities

print("\nTop cities:\n")
print(customers["City"].value_counts().head(10))

plt.figure()
customers["City"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Cities by Customers")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("reports/figures/top_cities.png")
plt.close()

#  Country distribution

print("\nCountry distribution:\n")
print(customers["Country"].value_counts())