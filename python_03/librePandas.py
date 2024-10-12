#Pandas: para el manaejo dea conjunto de datos
import pandas as pd
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
s.value_counts() : Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie s.
s.min() : Devuelve el menor de los datos de la serie s.
s.max() : Devuelve el mayor de los datos de la serie s.
s.mean() : Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico.
s.std() : Devuelve la desviación típica de los datos de la serie s cuando los datos son de un tipo numérico.
s.describe(): Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles.




