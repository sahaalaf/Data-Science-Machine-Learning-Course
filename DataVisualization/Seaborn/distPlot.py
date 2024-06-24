import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

titanic = sb.load_dataset("titanic")
passengers_age = titanic['age'].dropna()
sb.displot(passengers_age, bins = 30, kde = False)
plt.show()