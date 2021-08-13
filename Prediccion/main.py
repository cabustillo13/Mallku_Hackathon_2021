from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot as plt

print("######################\n## STOP THE FIRE 4+ ##\n######################\n")

"""Cargar información"""
df = pd.read_csv("Dataset_Excel2.csv", index_col=0)

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

"""Graficar el modelo"""
pd.plotting.scatter_matrix(df, c=y, figsize=(12, 12), marker='o', s=20, alpha=.8)
plt.show()

var = input("Ingrese Temperatura, Humedad, Viento: ")

"""¿Se produce o no se produce un incendio?"""
print(neigh.predict([[12, 50, 8]]))

"""Probabilidad que ocurra un incendio"""
print(neigh.predict_proba([[12, 50, 8]]))

"""
Datos de prueba:
7 de enero 2018     14.4, 60.2, 10
16 de sept 2018     9, 83 ,7
7 de dic 2018       12, 50, 8
"""