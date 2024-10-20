#dataframe
import pandas as pd
df = pd.read_csv(r'C:\Users\garci\Documents\Python_2024\python_04\data.csv')
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

#agregar una nueva columna co valores
df['diabetes'] = pd.Series([False,True], index=[0,1])

#aplicar funcioes a columnas
#esta crea una nueva columna con el doble de los valores de la columna colesterol
df['colesterol'] = df['colesterol'].apply(lambda x: x*2)
print(df)
#eliminar una columna
df = df.drop('diabetes', axis=1)

#convertir una columna a tipo datetime
df = pd.DataFrame({'Name': ['John', 'Steve', 'Sarah'], 'Nacimiento': ['2017-05-01', '2017-05-02', '2017-05-03']})
df['Nacimiento'] = pd.to_datetime(df['Nacimiento'])


#modificar formato fecha
df['Nacimiento'] = df['Nacimiento'].dt.strftime('%m/%d/%Y')
print(df)

#resumen descriptivo de un dataframe
#df.count() : Devuelve una serie número de elementos que no son nulos ni NaN en cada columna del DataFrame df.
#df.sum() : Devuelve una serie con la suma de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
#df.cumsum() : Devuelve un DataFrame con la suma acumulada de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
#df.min() : Devuelve una serie con los menores de los datos de las columnas del DataFrame df.
#df.max() : Devuelve una serie con los mayores de los datos de las columnas del DataFrame df.
#df.mean() : Devuelve una serie con las media de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
#df.std() : Devuelve una serie con las desviaciones típicas de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
#df.describe(include = tipo) : Devuelve un DataFrame con un resumen estadístico de las columnas del DataFrame df del tipo tipo. Para los datos numéricos (number) se calcula la media, la desviación típica, el mínimo, el máximo y los cuartiles de las columnas numéricas. Para los datos no numéricos (object) se calcula el número de valores, el número de valores distintos, la moda y su frecuencia. Si no se indica el tipo solo se consideran las columnas numéricas.
#pop() : Elimina la columna del DataFrame df y devuelve una serie con los datos de la columna eliminada.
#drop() : Elimina la columna del DataFrame df y devuelve un DataFrame con el resto de las columnas.

#filytrar datos
#df[df['edad'] > 20] : Devuelve un DataFrame con las filas del DataFrame df que cumplen la condición edad > 20.

#orddenar un dataframe
#df.sort_values(by = 'edad') : Devuelve un DataFrame con las filas del DataFrame df ordenadas por la columna edad.
#df.sort_values(by = ['edad', 'colesterol']) : Devuelve un DataFrame con las filas del DataFrame df ordenadas primero por la columna edad y luego por la columna colesterol.







