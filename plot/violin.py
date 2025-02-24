import matplotlib.pyplot as plt
import numpy as np

# Example data: Three categories with different distributions
category_1 = np.random.normal(0, 1, 100)  # Normal distribution with mean=0 and std=1
category_2 = np.random.normal(2, 1.5, 100)  # Normal distribution with mean=2 and std=1.5
category_3 = np.random.normal(4, 0.5, 100)  # Normal distribution with mean=4 and std=0.5

# Data to plot
data = [category_1, category_2, category_3]

# Create violin plot
plt.violinplot(data)

# Set axis labels and title
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot of Multiple Distributions")

# Show the plot
plt.show()
