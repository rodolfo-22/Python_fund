#Uso de librerias, numpy
import numpy as np

#corre esta celda para tener las arrays a trabajar
# Array unidimensional
arr_1d = np.array([10, 20, 30, 40, 50])

# Array bidimensional
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Array 1D:", arr_1d)
print("Array 2D:\n", arr_2d)
# Accede al primer elemento de arr_1d
print("Primer elemento de arr_1d:", arr_1d[0])
# Accede al último tercer elemento de arr_1d
print("Tercer elemento de arr_1d:", arr_1d[2])
#Extrae la matriz [2,3],[5,6]
print(arr_2d[:2,1:])
# Extrae los primeros tres elementos de arr_1d
subarray_1d = arr_1d[0:3]
print("Subarray de arr_1d:", subarray_1d)

# Extrae las primeras dos filas y las primeras dos columnas de arr_2d
subarray_2d = arr_2d[:2, 0:3]
print("Subarray de arr_2d:\n", subarray_2d)
# Filtra elementos mayores a 22 en la arr_1d
condicion = arr_1d[arr_1d>22]
print("Elementos mayores a 22:", condicion)

# Redimensiona arr_1d a un array de 5 filas y 1 columna
arr_1d_reshaped = arr_1d.reshape(5,1)
print("Array 1D redimensionado:\n", arr_1d_reshaped)

# Redimensiona arr_2d a un array de 1 fila y 9 columnas
arr_2d_reshaped = arr_2d.reshape(1,9)
print("Array 2D redimensionado:\n", arr_2d_reshaped)

#Crea dos arrays arr1 = [1, 2, 3, 4] y arr2 = [5, 6, 7, 8] 
# y realiza las siguientes operaciones:
arr1 = np.array([1, 2, 3, 4] ) 
arr2 = np.array([5, 6, 7, 8])
#suma el arr1 con el arr2
print(arr1 + arr2)
#resta de arrays
print(arr1 - arr2)
#multplicacion
print(arr1 * arr2)
#divicion
print(arr1 / arr2)
print(np.size(arr1))
#buscar la matriz transpuesta
print(arr_2d.T)
#Redimensiona arr_1d en un array de 5 filas y 1 columna.
first = arr_1d.reshape(5,1)
print(first)
#Redimensiona arr_2d en un array de 1 fila y 9 columnas.
second = arr_2d.reshape(1,9)
print(second)


#resorce
#https://colab.research.google.com/drive/1EXtnPappRy2yMlgUNZhSZ0p0oAQwUTfj?usp=sharing
#https://colab.research.google.com/drive/1NzxNresDb8q4GRSObZA2mNWLkeiJy1Rb?usp=sharing
#https://colab.research.google.com/drive/1e64j_gnhXZ5wM30f4eOi3QA-_kZmSel-?usp=sharing