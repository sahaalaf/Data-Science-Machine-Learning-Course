import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

df = sb.load_dataset("tips")
df.boxplot(by = 'day', column = ['total_bill'], grid = False)
plt.show()