import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print("Before Flattening Array: ", arr)
newArr = arr.reshape(-1)
print("After Flattening Array: ", newArr)