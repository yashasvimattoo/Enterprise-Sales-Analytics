import pandas as pd
df = pd.read_csv("data/raw/retail_data.csv")
customers = df[[
'Customer_ID','Name','Email','Phone','Address','City','State',
'Zipcode','Country','Age','Gender','Income','Customer_Segment'
]]

customers.to_csv("data/processed/customers.csv", index=False)

products = df[[
'Product_Category','Product_Brand','Product_Type','products'
]]
products = products.rename(columns={"products": "Product_Name"})

products.to_csv("data/processed/products.csv", index=False)

sales = df[[
'Transaction_ID','Customer_ID','Date','Year','Month','Time',
'Total_Purchases','Amount','Total_Amount','Product_Category',
'Shipping_Method','Payment_Method','Order_Status','Ratings','Feedback'
]]

sales = sales.merge(
    df[['Transaction_ID', 'products']],
    on='Transaction_ID',
    how='left'
).rename(columns={"products": "Product_Name"})

sales.to_csv("data/processed/sales.csv", index=False)


print("Dataset split successfully")