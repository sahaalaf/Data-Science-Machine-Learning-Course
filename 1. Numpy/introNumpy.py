import numpy as np
a = np.array(2)
b = np.array([1,2,3])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print("A Dimension is: ", a.ndim, " Shape is: ", a.shape)
print("B Dimension is: ", b.ndim, " Shape is: ", b.shape)
print("C Dimension is: ", c.ndim, " Shape is: ", c.shape)
print("D Dimension is: ", d.ndim, " Shape is: ", d.shape)