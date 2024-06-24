import pandas as pd
df =  pd.read_csv('D:/Machine Learning/Data-Science-Machine-Learning-Course/4. DataProcessing/data_set.csv')

## before handling missing values
print("Before Handling Missing Value with the Median:")
print(df.isnull().sum())

## handle missing values using mode
df['salary'] = df['salary'].fillna(df['salary'].mode()[0])

## after handle missing values
print("After Handling Missing Value with the Median:")
print(df.isnull().sum())

## print after missing values being handled
print(df.head())