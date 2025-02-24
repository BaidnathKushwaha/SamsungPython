import numpy as np

# Problem1: Finding indices where spendings are greater than 100

# Explanation: Using np.where() to find indices where the condition is met

week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
high_spend = np.where(week_spendings > 100)
print(high_spend) # Output: Indices where the values are greater than 100