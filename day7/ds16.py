# Create a checkerboard 8x8 matrix using the tile function 
import numpy as np

#my_matrix = np.array([[0,1],[1,0]])
#print(my_matrix)

chess_board = np.tile( np.array([[1, 0],[0, 1]]), (4,4))
# chess_board = np.tile( np.array([['*', ' '],[' ', '*']]), (4,4))
#print('\n', chess_board)

list1 = []
for array in chess_board:
    list1 = list(array)
    string = ' '.join(map(str, list1))
    print(string)