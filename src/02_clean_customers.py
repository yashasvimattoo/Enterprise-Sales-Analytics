import pandas as pd

# load data
customers = pd.read_csv("data/processed/customers.csv")

# -------------------------
# 1 Remove duplicate customers
# -------------------------
customers = customers.drop_duplicates(subset="Customer_ID")

# -------------------------
# 2 Remove rows with missing Customer_ID
# -------------------------
customers = customers.dropna(subset=["Customer_ID"])

# -------------------------
# 3 Replace blank spaces with NaN
# -------------------------
customers = customers.replace(r'^\s*$', None, regex=True)

# -------------------------
# 4 Fill missing values
# -------------------------
customers["Email"] = customers["Email"].fillna("Unknown")
customers["Phone"] = customers["Phone"].fillna("Unknown")
customers["Address"] = customers["Address"].fillna("Unknown")
customers["Name"] = customers["Name"].fillna("Unknown Customer")

customers["City"] = customers["City"].fillna("Unknown")
customers["State"] = customers["State"].fillna("Unknown")
customers["Country"] = customers["Country"].fillna("Unknown")

customers["Customer_Segment"] = customers["Customer_Segment"].fillna("Regular")

# -------------------------
# 5 Fix text formatting
# -------------------------
customers["City"] = customers["City"].str.strip().str.title()
customers["State"] = customers["State"].str.strip().str.title()
customers["Country"] = customers["Country"].str.strip().str.title()

# -------------------------
# 6 Clean Gender values
# -------------------------
customers["Gender"] = customers["Gender"].str.strip().str.title()
customers["Gender"] = customers["Gender"].fillna("Unknown")

# -------------------------
# 7 Handle Age
# -------------------------
customers["Age"] = pd.to_numeric(customers["Age"], errors="coerce")

customers.loc[(customers["Age"] < 10) | (customers["Age"] > 90), "Age"] = None

customers["Age"] = customers["Age"].fillna(customers["Age"].median())

# -------------------------
# 8 Handle Income
# -------------------------
# clean income category
customers["Income"] = customers["Income"].str.strip().str.title()

# fill missing values
customers["Income"] = customers["Income"].fillna("Unknown")
# -------------------------
# 9 Zipcode validation
# -------------------------
customers["Zipcode"] = customers["Zipcode"].astype(str)

# -------------------------
# 10 Final check
# -------------------------
print("Missing values after cleaning:")
print(customers.isnull().sum())

print("Dataset shape:", customers.shape)

# save cleaned data
customers.to_csv("data/processed/customers_cleaned.csv", index=False)

print("Customers dataset cleaned successfully")