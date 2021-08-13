import pandas as pd

"""Load Dataframe"""
# opening the CSV file
df = pd.read_csv("Dataset_Excel.csv", index_col=0)

"""Definir variables"""
temperatura = list(df.Temperatura)
viento = list(df.Viento)
humedad = list(df.Humedad)

# display DataFrame
print(df)

# access to one column
print(list(df.Temperatura))

"""Get metadata of the CSV"""
# get metadata of DataFrame
print(df.info())

"""Select rows from CSV"""
# select top 2 rows
print(df.head(2))

# select bottom 2 rows
print(df.tail(2))

"""Get element from DataFrame"""
# get a element using row and column labels
print(df.at[1, 'Temperatura'])