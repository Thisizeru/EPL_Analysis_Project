import pandas as pd
import pyarrow
import glob
cleaned_dataset=pd.read_parquet("Online_Retail_Store\Datasets\Cleaned_Retail_dataset.parquet")
print(cleaned_dataset)

#PRODUCT PERFORMANCE
#1.Top 10 most sold product by quantity
Top10_sold_product=cleaned_dataset[["Description","Quantity"]]
Top10_sold_product=cleaned_dataset.groupby("Description")["Quantity"].sum().nlargest(10).reset_index()
print(Top10_sold_product)
Top10_sold_product.to_csv("Top10_sold_product.csv",index=False)

#2 Top 10 Product By Revenue
cleaned_dataset["Total_Revenue"]=cleaned_dataset["Quantity"] * cleaned_dataset["UnitPrice"]
print(cleaned_dataset["Total_Revenue"])
changes={"Total_Revenue" :"Total Revenue"}
cleaned_dataset.rename(columns=changes, inplace=True)

print(cleaned_dataset[["Description","UnitPrice","Total Revenue"]])

EDA_Revenue=(cleaned_dataset.groupby("Description")["Total Revenue"].sum().nlargest(10).reset_index())
Top_10_Revenue=EDA_Revenue.sort_values("Total Revenue",ascending=False).head(10)

Top_10_Revenue.to_csv("Top_10_Revenue.csv", index=False)

#Total Revenue per month 
cleaned_dataset["YearMonth"]= cleaned_dataset["InvoiceDate"].dt.to_period('M')
print("Columns:",cleaned_dataset.columns.tolist())
print(cleaned_dataset.head(3))
print(cleaned_dataset.columns)
print(cleaned_dataset[["InvoiceDate","YearMonth"]].head())
sales_per_month = cleaned_dataset.groupby("YearMonth")["Total Revenue"].sum().sort_index()
print(sales_per_month)

sales_per_month.index= sales_per_month.index.to_timestamp()

#visualizing Revenue per Month
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(sales_per_month.index,
         sales_per_month.values, 
         marker='o')
plt.title("Revenue Monthly Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.show()

#Revenue Trend by country
sales_by_country = cleaned_dataset.groupby("Country")["Total Revenue"].sum().sort_values(ascending=False).nlargest(10)
print(sales_by_country)

#country with the most customers
most_customers_origin=(
    cleaned_dataset.groupby("Country")["CustomerID"]
    .nunique()
    .nlargest(10)
    .reset_index()
    )

print(most_customers_origin)
print(cleaned_dataset)
#most_customers_origin.to_csv("most customers_origin.csv",index=False)

countries_with_less_customers=(
    cleaned_dataset.groupby("Country")["CustomerID"]
    .nunique()
    .nsmallest()
    .reset_index()
 )
print(countries_with_less_customers)  

#analysis to show high valued customers and potential vip for retention
customer_revenue = cleaned_dataset.groupby("CustomerID")["UnitPrice"].sum().nlargest(10).reset_index().sort_values("UnitPrice", ascending= False)
print(customer_revenue)
customer_revenue.to_csv("customer_revenue.csv", index =False )

customer_frequency=cleaned_dataset.groupby("CustomerID")["InvoiceNo"].nunique().reset_index().sort_values("InvoiceNo",ascending=False)
print(customer_frequency)
customer_frequency.to_csv("customer_frequency.csv",index = False)

#Checking for correlation between price and quantity
correlation=cleaned_dataset[["Quantity", "UnitPrice"]].corr()
print(correlation)
correlation.to_csv("correlation.csv",index=False)

cleaned_dataset.to_csv("analyzed_Retailed_dataset.csv",index=False)
cleaned_dataset.to_parquet("analyzed_Retailed_dataset.parquet", index=False)


#print(cleaned_dataset)
#print(cleaned_dataset.columns)

print(cleaned_dataset["YearMonth"])
