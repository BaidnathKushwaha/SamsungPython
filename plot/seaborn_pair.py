# SEABORN PAIR PLOT
# Problem Statement: Analyzing relationships between multiple stock market variables.
# Question: How do different variables relate to each other in the dataset?

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_dict = {
    "total_bill": np.random.uniform(5, 50, 100),
    "tip": np.random.uniform(1, 10, 100),
    "sex": np.random.choice(["Male", "Female"], 100),
    "smoker": np.random.choice(["Yes", "No"], 100),
    "day": np.random.choice(["Thur", "Fri", "Sat", "Sun"], 100),
    "time": np.random.choice(["Lunch", "Dinner"], 100),
    "size": np.random.randint(1, 6, 100)
}

# Convert dictionary to DataFrame
data_df = pd.DataFrame(data_dict)

# Create pair plot using seaborn
sns.pairplot(data_df, hue="sex")
plt.title("Pair Plot")
plt.show()
