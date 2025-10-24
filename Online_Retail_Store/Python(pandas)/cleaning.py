import pandas as pd
import pyarrow
df=pd.read_csv("Online_UK_and_France_Retail\Datasets\online_retail.csv")
print(df)


print(df.info())

#changing invoicedate from object to date
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"],errors="coerce")

#changing stockcode from objext

print(df.info())

#Droping columns with NA values


dropingna=df.dropna(subset= ["UnitPrice","CustomerID","InvoiceDate"],inplace=True)
                
print(dropingna)


print(df.isna().sum())

print(df["CustomerID"].isna().sum())

print(df)

duplicates = df[df.duplicated()]
print(duplicates)
print(df)
#The Dataset is not so messy and the columns with duplicate values is the invoiceno column and that is undertandable due to one customer using one invoice number to buy more than one product

df.to_csv("Cleaned_Retail_dataset.csv",index=False)
df.to_parquet("Cleaned_Retail_dataset.parquet",index=False)
print(df.info())

