import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Before Dimensions: ", arr.ndim)
print("Before Shape: ", arr.shape)
print("Array Before Reshape: ", arr)
newArray = arr.reshape(4,3)
print("After Dimensions: ", newArray.ndim)
print("After Shape: ", newArray.shape)
print("Array After Reshape: ", newArray)