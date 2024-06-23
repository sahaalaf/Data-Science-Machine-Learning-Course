import numpy as np
## access elements in 1-D Array
one_dim_array = np.array([1,2,3,4,5,6])
print('6th Element: ', one_dim_array[5])

## access elements in 2-D Array
two_dim_array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('4 Element of 2nd Row: ', two_dim_array[1,3])

## access elements in 3-D Array
three_dim_array = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print('2 Element of 2nd Row: ', three_dim_array[1,1])
