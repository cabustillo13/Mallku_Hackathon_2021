from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

"""Cargar información"""
df = pd.read_csv("Dataset_Excel.csv", index_col=0)

"""Armar el dataset -> Variables"""
X = []
y = []
# Cantidad de filas: len(df)
for i in range(len(df)):
    X.append([])
    # Cantidad de columnas: 3
    X[i].append(df.at[i+1, 'Temperatura'])
    X[i].append(df.at[i+1, 'Humedad'])
    X[i].append(df.at[i+1, 'Viento'])

y = list(df.Focos)

"""Procedimiento para KNN"""
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
KNeighborsClassifier(...)

"""¿Se produce o no se produce un incendio?"""
print(neigh.predict([[2.1, 3.4, 6.7]]))

"""Probabilidad que ocurra un incendio"""
print(neigh.predict_proba([[2.1, 3.4, 6.7]]))
