# HORIZONTAL BAR PLOT
# Problem Statement: Displaying categorical data with long labels in a horizontal format.
# Question: Which category has the highest value in the horizontal bar chart?


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.barh(categories, values, color='orange')
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart")
plt.show()