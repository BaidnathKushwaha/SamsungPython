#Difference between np.arange() and np.linspace()
import numpy as np
# Explanation: np.arange() generates values with a fixed step, while np.linspace() generates a set number of equally spaced values

sequence_arange = np.arange(1, 10, 3)  # Generates values from 1 to 10 with a step of 3
sequence_linspace = np.linspace(0, 100, 5)  # Generates 5 equally spaced values between 0 and 100
print("Using arange:", sequence_arange)
print("Using linspace:", sequence_linspace)