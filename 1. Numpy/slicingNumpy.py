import numpy as np

# slice 1-D Array
one_dim_array = np.array([1,2,3,4,5,6,7,8,9,10])
print('Slice From 2nd Index to 5th(Skip 1 Element): ', one_dim_array[1:9:2])

# slice 2-D Array
two_dim_array = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
print('Slice Column 2 to Column 9 of Row 1: ',two_dim_array[0, 1:9])
print('Slice Column 5 to Column 9 of Row 2: ',two_dim_array[1, 5:9])

# slice 3-D Array
three_dim_array = np.array([[[1,2,3], [4,5,6],[7,8,9], [10,11,12]], [[13,14,15], [16,17,18],[19,20,21], [22,23,24]]])
print('Slice Column 1 to Column 3 of Row 1: ',three_dim_array[0, 0:3])
print('Slice Column 1 to Column 2 of Row 2: ',three_dim_array[1, 0:2])