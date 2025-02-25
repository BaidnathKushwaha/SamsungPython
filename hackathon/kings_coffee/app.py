import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\learning\python\SamsungPython\hackathon\kings_coffee\coffee_sales.csv")
# Ensure you have a CSV file with the required data

# (a) Best Coffee Seeds Supplier Analysis
supplier_performance = df.groupby('Supplier').agg({'Seeds Purchased': 'sum', 'Revenue': 'sum'}).reset_index()
best_supplier = supplier_performance.sort_values(by='Revenue', ascending=False).iloc[0]
print("Best Supplier:", best_supplier)

# (b) Compare Sales of Instant Coffee vs. Filter Coffee
coffee_type_sales = df.groupby('Coffee Type')['Sales'].sum().reset_index()
plt.figure(figsize=(6, 4))
sns.barplot(data=coffee_type_sales, x='Coffee Type', y='Sales', palette='coolwarm')
plt.title("Sales Comparison: Instant vs. Filter Coffee")
plt.show()

# (c) Customer Feedback on Water Quantity
water_feedback = df.groupby('Water Quantity')['Customer Rating'].mean().reset_index()
plt.figure(figsize=(6, 4))
sns.lineplot(data=water_feedback, x='Water Quantity', y='Customer Rating', marker='o')
plt.title("Customer Feedback on Water Quantity")
plt.xlabel("Water Quantity")
plt.ylabel("Average Customer Rating")
plt.show()

# (d) Compare Sales of Coffee with Sugar, Jaggery, and Sugar-Free
sweetener_sales = df.groupby('Sweetener Type')['Sales'].sum().reset_index()
plt.figure(figsize=(6, 4))
sns.barplot(data=sweetener_sales, x='Sweetener Type', y='Sales', palette='viridis')
plt.title("Sales Comparison: Sugar vs. Jaggery vs. Sugar-Free")
plt.show()































