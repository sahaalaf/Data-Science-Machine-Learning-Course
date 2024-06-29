import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('D:/Machine Learning/Data-Science-Machine-Learning-Course/4. DataProcessing/iris.csv')
le = LabelEncoder()
df['variety'] = le.fit_transform(df['variety'])
print(df.head(100))