# amazon_ecommerce_analysis.py
# Brooo E-commerce Sales Data Analysis Project
# Author: Manimozhi Jeganathan
# AI & DS 4th Sem | GitHub ready

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
data = pd.read_csv("amazon_sales_dataset.csv")  # replace with your file name
print("Data Loaded Successfully!\n")
print(data.head())
print(data.info())

# -----------------------------
# Step 2: Data Cleaning
# -----------------------------
# Drop missing values
data.dropna(inplace=True)

# Drop duplicates
data.drop_duplicates(inplace=True)

# Convert date to datetime
data['order_date'] = pd.to_datetime(data['order_date'])

print("\nData cleaned ✅\n")

# -----------------------------
# Step 3: Exploratory Analysis
# -----------------------------

# Top 5 Products by Total Revenue
top_products = data.groupby('product_id')['total_revenue'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products by Revenue:\n", top_products)

# Top 5 Product Categories by Revenue
top_categories = data.groupby('product_category')['total_revenue'].sum().sort_values(ascending=False)
print("\nRevenue by Product Category:\n", top_categories)

# Top 5 Customer Regions by Revenue
top_regions = data.groupby('customer_region')['total_revenue'].sum().sort_values(ascending=False).head(5)
print("\nTop Customer Regions:\n", top_regions)

# Monthly Revenue Trend
monthly_revenue = data.groupby(data['order_date'].dt.to_period('M'))['total_revenue'].sum()
plt.figure(figsize=(10,5))
monthly_revenue.plot(kind='line', marker='o', color='green')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png")
plt.show()

# Product Category-wise Revenue
plt.figure(figsize=(8,5))
top_categories.plot(kind='bar', color='skyblue')
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.show()

# -----------------------------
# Step 4: Insights
# -----------------------------
print("\nInsights:")
print("- Top 5 products generate the highest revenue.")
print("- Certain months have peak revenue indicating seasonal trends.")
print("- Some regions contribute more to total revenue than others.")
print("- Product category analysis highlights most profitable categories.")

# -----------------------------
# Step 5: Optional Bonus Analysis
# -----------------------------
# Average rating by category
avg_rating = data.groupby('product_category')['rating'].mean().sort_values(ascending=False)
print("\nAverage Rating by Category:\n", avg_rating)

# Total quantity sold by category
quantity_category = data.groupby('product_category')['quantity_sold'].sum().sort_values(ascending=False)
print("\nTotal Quantity Sold by Category:\n", quantity_category)


