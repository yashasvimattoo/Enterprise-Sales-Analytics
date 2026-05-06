import pandas as pd


customers = pd.read_csv("data/processed/customers.csv")

customers = customers.drop_duplicates(subset="Customer_ID")


customers = customers.dropna(subset=["Customer_ID"])


customers = customers.replace(r'^\s*$', None, regex=True)


customers["Email"] = customers["Email"].fillna("Unknown")
customers["Phone"] = customers["Phone"].fillna("Unknown")
customers["Address"] = customers["Address"].fillna("Unknown")
customers["Name"] = customers["Name"].fillna("Unknown Customer")

customers["City"] = customers["City"].fillna("Unknown")
customers["State"] = customers["State"].fillna("Unknown")
customers["Country"] = customers["Country"].fillna("Unknown")
customers["Customer_Segment"] = customers["Customer_Segment"].fillna("Regular")


customers["City"] = customers["City"].str.strip().str.title()
customers["State"] = customers["State"].str.strip().str.title()
customers["Country"] = customers["Country"].str.strip().str.title()


# Clean Gender values

customers["Gender"] = customers["Gender"].str.strip().str.title()
customers["Gender"] = customers["Gender"].replace({
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female"
})
customers["Gender"] = customers["Gender"].fillna("Unknown")

#  Handle Age

customers["Age"] = pd.to_numeric(customers["Age"], errors="coerce")

customers.loc[(customers["Age"] < 10) | (customers["Age"] > 90), "Age"] = None

customers["Age"] = customers["Age"].fillna(customers["Age"].median())

# Handle Income

customers["Income"] = customers["Income"].str.strip().str.title()
customers["Income"] = customers["Income"].fillna("Unknown")

customers["Zipcode"] = customers["Zipcode"].astype(str).str.strip()


print("Missing values after cleaning:")
print(customers.isnull().sum())

print("Dataset shape:", customers.shape)

customers.to_csv("data/processed/customers_cleaned.csv", index=False)

print("Customers dataset cleaned successfully")