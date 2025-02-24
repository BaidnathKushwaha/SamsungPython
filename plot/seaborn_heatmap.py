# SEABORN HEATMAP
# Problem Statement: Understanding correlations between different financial factors.
# Question: Which two variables have the highest positive correlation?


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Sample DataFrame for demonstration
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
}

# Create the DataFrame
data_df = pd.DataFrame(data)

# Compute correlation matrix
corr = data_df.corr()

# Create heatmap with correlation values
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap")
plt.show()