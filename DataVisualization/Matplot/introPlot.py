import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3])
y = np.array([2,23,100])

## dotted plot
plt.plot(x,y, linestyle = "dotted")
plt.show()