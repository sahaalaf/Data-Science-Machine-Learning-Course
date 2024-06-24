import pandas as pd
df = pd.read_csv('airport.csv')
## print all csv file
print(df)

## print first 10 rows
print(df.head(10))

## print last 20 rows
print(df.tail(20))

## info about dataset
print(df.info())

# description of data (statistic for numeric data)
print(df.describe())

## relations b/w each column
print(df.corr())