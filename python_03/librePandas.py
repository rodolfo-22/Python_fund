#Pandas: para el manaejo dea conjunto de datos
import pandas as pd
import numpy as np
#Las principales características de esta librería son:

#Manipulación de datos estructurados de forma rápida.
#Integración con librerías de visualización y otros paquetes de Python.
#Funcionalidades para limpieza de datos, transformación, agrupación, y análisis estadístico.
#Permite leer y escribir fácilmente ficheros en formato CSV, Excel y bases de datos SQL.
#Integración con librerías de visualización y otros paquetes de Python.
#Permite acceder a los datos mediante índices o nombres para filas y columnas.
#Ofrece métodos para reordenar, dividir y combinar conjuntos de datos.

#una serie es un objeto de una sola dimensión que puede contener cualquier tipo de datos
#un DataFrame es un objeto de dos dimensiones, similar a una tabla de una base de datos

#como se crea una serie
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)
print(type(s))
#para imprimir un dato de la serie
print(s[0])
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s.size)
print(s.index)
print(s.values)
#El acceso a los elementos de un objeto del tipo Series puede ser a través de posiciones o través de índices (nombres).

#Las siguientes funciones permiten resumir varios aspectos de una serie:

#s.count() : Devuelve el número de elementos que no son nulos ni NaN en la serie s.
#s.sum() : Devuelve la suma de los datos de la serie s cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
#s.cumsum() : Devuelve una serie con la suma acumulada de los datos de la serie s cuando los datos son de un tipo numérico.
#s.value_counts() : Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie s.
#s.min() : Devuelve el menor de los datos de la serie s.
#s.max() : Devuelve el mayor de los datos de la serie s.
#s.mean() : Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico.
#s.std() : Devuelve la desviación típica de los datos de la serie s cuando los datos son de un tipo numérico.
#s.describe(): Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles.

s1 = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
#s2 = pd.Series([1, 2, 2, 3, 3, 3, np.nan, 4, 4, 4, 4])

print(s1.sum())
print(s1.cumsum())
print(s1.value_counts())
print(s1.min())
print(s1.max())
print(s1.mean())
print(s1.std())
print(s1.describe())

#aplicar operaciones a una serie
s = pd.Series([1, 2, 3, 4, 5])
print(s)
print(s + 10)
print(s * 10)
print(s / 10)
print(s ** 2)
print(s % 2)
print(s > 2)
print(s < 2)
print(s == 2)
print(s != 2)

#aplicar funciones a una serie
#s.apply(f) : Devuelve una serie con el resultado de aplicar la función f a cada uno de los elementos de la serie s.
# Serie de números enteros
serie = pd.Series([2, 4, 6, 8, 10])

# Elevar cada elemento al cuadrado
print(serie.apply(np.square))
# Calcular el logaritmo natural de cada elemento
print(serie.apply(np.log))

s = pd.Series(['a', 'b', 'c'])
s = s.apply(str.upper)
print(s)

#filtrado de una serie
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
s2 = pd.Series(['Trimestre 1', 'Trimestre 2', 'Trimestre 1'])
#extraer los valores que cumplen con la condición
print(s[s > 5])
print(s2 == 'trimestre 1')

#ordenar una serie
s.sort_values(ascending=False)
print(s)
s.sort_index(ascending = True)
print(s)

#eliminar
s = pd.Series(['a', 'b', None, 'c', np.nan,  'd'])
print(s)
#este elimina los valores nulos dentro de una serie
s = s.dropna()
print(s)

#dataframe
#Es una estructura de datos bidimensional, similar a una tabla, donde cada columna puede 
#contener un tipo de dato diferente. Es la estructura principal de pandas para manipular datos.

datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
         'edad':[18, 22, 20, 23],
         'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
         'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
         }
df = pd.DataFrame(datos)
print(df)


df2 = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df2)

df3 = pd.DataFrame([{'Apellido':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])
print(df3)

df4 = pd.DataFrame(np.random.randn(4,4), columns=['a', 'b', 'c', 'd'])
print(df4)  


