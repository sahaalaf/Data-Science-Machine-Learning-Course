import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

data = sb.load_dataset("mpg")
sb.regplot(x = 'mpg', y = 'acceleration', data = data)
plt.show()