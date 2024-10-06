import numpy as np
import pandas as pd

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

suma = a + b  # [5, 7, 9]
resta = a - b  # [-3, -3, -3]
multiplicacion = a * b  # [4, 10, 18]
division = a / b  # [0.25, 0.4, 0.5]

print(suma, resta, multiplicacion, division)

# Crear un arreglo de ceros y unos
ceros = np.zeros((3, 3))
unos = np.ones((2, 2))
print(ceros)
print(unos)

#array, multidimencionales, solo puede ser de un tipo de dato
import numpy as np
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)

#indexar array, es extraer un valor de un array
arr = np.array([10, 20, 30, 40, 50])

# Acceder a un elemento específico
print(arr[0])  # Salida: 10
print(arr[3])  # Salida: 40

# Modificar un elemento
arr[2] = 100
print(arr)  # Salida: [ 10  20 100  40  50]

arr = np.array([10, 20, 30, 40, 50])

# Seleccionar un rango de elementos
print(arr[1:4])  # Salida: [20 30 40]

# Seleccionar elementos con un paso
print(arr[::2])  # Salida: [10 30 50] (salta cada dos elementos)

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Seleccionar una fila completa
print(matriz[1, :])  # Salida: [4 5 6] (segunda fila completa)

# Seleccionar una columna completa
print(matriz[:, 2])  # Salida: [3 6 9] (tercera columna completa)

# Seleccionar un subarreglo (primeras dos filas, dos primeras columnas)
sub_matriz = matriz[0:2, 0:2]
print(sub_matriz)
# Salida:
# [[1 2]
#  [4 5]]

#manipulacion de arrays
man = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


#unir arrays/ concatenar
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_concat = np.concatenate((arr1, arr2))

#dividir
arr_div = np.array_split(arr, 2)

#axis 1 columnas, axis 0 filas
arr_h = np.hstack((arr1, arr2))
arr_v = np.vstack((arr1, arr2))
print(arr_h)
print(arr_v)

#estadisticas
print(np.mean(arr))
print(np.median(arr))   

#broadcasting, es una forma de hacer operaciones entre arrays de diferentes tamaños
#sumar unn array con un int
arr = np.array([1, 2, 3])
resultado = arr + 1
print(resultado)  # Salida: [2 3 4]

#multiplicacion de arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 * arr2
print(resultado)  # Salida: [ 4 10 18]

#multiplicacion de 1d con 2d
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6], [7, 8, 9]])
resultado = arr1 * arr2
print(resultado)



#crear array con los numeros de 1 a 20
arr = np.arange(1, 21)

#trasnformalo a que sea de 2 filas y 5 columnas
arr = arr.reshape(2, 5)
print(arr)

import numpy as np

# Crear un array plano de 10 elementos
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Reorganizarlo en una matriz de 2 filas y 5 columnas
matriz = arr.reshape(2, 5)

print(matriz)
