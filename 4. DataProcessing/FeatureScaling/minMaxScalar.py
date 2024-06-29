import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame({'Weight':[15,18,12,10],'Price':[1,3,2,5]}, index = ['Orange', 'Apple', "Peace", 'Banana'])
scalar = MinMaxScaler()

df = pd.DataFrame(scalar.fit_transform(data), columns = ['Weight', 'Price'], index = ['Orange', 'Apple', "Peace", 'Banana'])

## before scaling
ax = data.plot.scatter(x='Weight', y='Price', color=['red','green','blue','yellow'], marker= '*', s=80, label="Before Scaling")

## after scaling
df = df.plot.scatter(x='Weight', y='Price', color=['red','green','blue','yellow'], marker= 'o', s=60, label="After Scaling", ax=ax)

plt.axhline(0, color='red',alpha=0.2)
plt.axvline(0, color='red',alpha=0.2)
plt.show()