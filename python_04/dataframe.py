#dataframe
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

#Imprime los primeros cinco registros del DataFrame.
print("Primeros cinco registros:\n", df.head(5))
#iloc: permite seleccionar un subconjunto de filas y columnas de un DataFrame.
#iloc comprende por la posisocion de los elementos
print(df.iloc[1,:])
print(df.iloc[2]) #imprime la fila 2
print(df.iloc[0:3]) #imprime las primeras tres filas
print(df.iloc[:,0]) #imprime la columna 0

#loc: permite seleccionar un subconjunto de filas y columnas de un DataFrame.
#loc se guia por el nombre de las columnas
print(df.loc[1,:])
print(df.loc[1000,'nombre y apellido']) #imprime la fila 2
print(df.loc[:3,'colesterol', 'edad']) #imprime las primeras tres filas
print(df['colesterol'].mean())     #imprime el promedio de la columna colesterol


