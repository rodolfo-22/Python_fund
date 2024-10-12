#Crea una Serie de precios de algunos artículos usando una lista. 
# Los productos son "Laptop", "Teléfono", "Tablet" y "Monitor", con precios 
# de 1200, 800, 300 y 400, respectivamente.
import pandas as pd
s = pd.Series([1200, 800, 300, 400], index = ["Laptop", "Teléfono", "Tablet", "Monitor"])
print(s)    

#Crea una Serie a partir de un diccionario donde las claves sean los nombres de 
# los productos y los valores, la cantidad en stock. Usa estos valores: 
# "Laptop": 10, "Teléfono": 25, "Tablet": 15, "Monitor": 20. Atributos de una 
# Serie:
s2 = pd.Series({"Laptop": 10, "Teléfono": 25, "Tablet": 15, "Monitor": 20})
print(s2)

#Imprime los índices y valores de la Serie de precios que creaste. 
# ¿Cuál es el tipo de datos de esta Serie?
print(s.index)
print(s.values)
print(type(s))

#Accede al precio del "Teléfono" en la Serie de precios.
print(s["Teléfono"])

#Genera un resumen estadístico de la Serie de precios. 
# ¿Cuál es el precio promedio?
print(s.describe())
