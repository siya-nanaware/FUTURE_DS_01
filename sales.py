import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("online_retail.csv", encoding="ISO-8859-1")

df = df.dropna(subset=["CustomerID"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(10,5))
monthly_revenue.plot()
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_countries.plot(kind="bar")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_countries.png")
plt.close()

summary = pd.DataFrame({
    "Total Revenue": [df["Revenue"].sum()],
    "Total Orders": [df["InvoiceNo"].nunique()],
    "Total Customers": [df["CustomerID"].nunique()]
})

summary.to_csv("business_summary.csv", index=False)

print("Business Sales Performance Analysis Completed Successfully")