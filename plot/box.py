# BOX PLOT
# Problem Statement: Displaying data distribution and outliers using a box plot.
# Question: Which category has the highest spread in the dataset?
import matplotlib.pyplot as plt
import numpy as np
# Generate random data for 4 categories
data = [np.random.randn(100) for _ in range(4)]

# Create box plot
plt.boxplot(data, patch_artist=True)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()