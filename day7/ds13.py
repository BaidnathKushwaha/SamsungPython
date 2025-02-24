# Grouping data in a DataFrame and applying aggregate functions

# Explanation: Using groupby() and agg() to perform multiple aggregations on grouped data

import pandas as pd

data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [60000, 55000, 70000, 58000, 75000]
}

df = pd.DataFrame(data)

# Grouping by Department and calculating mean, sum, and max salary
grouped_df = df.groupby('Department').agg({'Salary': ['mean', 'sum', 'max']})  
print(grouped_df)
