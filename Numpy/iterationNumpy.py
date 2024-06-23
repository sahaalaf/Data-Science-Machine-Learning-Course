import numpy as np

# iteration through each element in 1-D Array
arr = np.array([1,2,3,4,5])
print("1-D Iteration is:")
for i in arr:
    print(i)

# iteration through each element in 2-D Array
arr_two_dim = np.array([[1,2,3,4],[5,6,7,8]])
print("2-D Iteration is:")
for i in arr_two_dim:
    for j in i:
        print(j)

# iteration through each element in 3-D Array
three_dim_array = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print("3-D Iteration is:")
for i in three_dim_array:
    for j in i:
        for k in j:
            print(k)