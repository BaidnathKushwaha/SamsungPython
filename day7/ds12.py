import numpy as np

np_array_data = np.array([[1, 2, 3, 4, 5,], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 3, 5, 7, 11], [11, 13, 17, 19, 23]], int)

print(np_array_data[:, 3])
print(np_array_data[1:4, 3])
print(np_array_data[:, 2:3])
print(np_array_data[1:, 1:4])