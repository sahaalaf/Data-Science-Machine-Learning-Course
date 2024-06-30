import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

## load data set
ds = pd.read_csv("D:/Machine Learning/Data-Science-Machine-Learning-Course/5. MachineLearning/Salary_Data.csv")
x = ds.iloc[:,:-1].values
y = ds.iloc[:,1].values

## testing on 80% data set
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)
regression = LinearRegression()
regression.fit(x_train, y_train)
y_predict = regression.predict(x_test)
x_predict = regression.predict(x_train)

plt.title = "Train on 80% Data"
plt.scatter(x_train, y_train, color="green")
plt.plot(x_train, x_predict, color="red")
plt.show()

plt.title = "30% Test Data"
plt.scatter(x_test, y_test, color="green")
plt.plot(x_train, x_predict, color="red")
plt.show()

print(ds.head(80))