# PIE CHART
# Problem Statement: Representing the market share of different brands.
# Question: Which brand has the largest market share?

# Define sizes and labels for pie chart

import matplotlib.pyplot as plt
sizes = [30, 20, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['blue', 'red', 'green', 'purple']

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.show()