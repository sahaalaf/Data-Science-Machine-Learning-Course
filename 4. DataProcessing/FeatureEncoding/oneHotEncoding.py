import pandas as pd
df = pd.read_csv('D:/Machine Learning/Data-Science-Machine-Learning-Course/4. DataProcessing/airport.csv')
a = pd.get_dummies(df, columns=['type'])
print(a)