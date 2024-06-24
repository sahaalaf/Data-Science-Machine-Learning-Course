import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Babar", "Virat", "Rohit", "Fakhar"])
y = np.array([16700, 26300, 21900, 9299])
plt.pie(y, labels=x)
plt.title("Cricketers Internationals Runs", style = "italic")
plt.show(), 