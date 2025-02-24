# Normalize a 5x5 random matrix
import numpy as np

my_array = np.random.random((5,5))
#print(my_array)

values = my_array - np.mean (my_array)
print('\n', values)

values = np.std (my_array)
print('\n', values)

my_array = (my_array - np.mean (my_array)) / (np.std (my_array))
print(my_array)