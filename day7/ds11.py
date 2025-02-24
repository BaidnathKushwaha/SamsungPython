# Creating a DataFrame

# Explanation: Using pandas to create a DataFrame from a dictionary

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)
print(df.isnull())  # Identifies missing values
print(df.isnull().sum())  # Counts missing values per column