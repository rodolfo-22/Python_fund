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

#Aplica una función a la Serie de precios para aumentar cada precio en un 5%.
s = s.apply(lambda x: x * 1.05)
print(s)
#
print("Mostar los productos con un precio mayor a 500.")
print(s[s>500])
#Ordena la Serie de precios en orden ascendente.
print("mostrar en orden ascendente")
print(s.sort_values())
print("mostrar en orden descendente")
print(s.sort_values(ascending=False))

#DataFrame
#Crea un DataFrame a partir de una lista de listas que incluya información sobre
# cada producto: el nombre, el precio y el stock. Agreguen los valores de su 
# preferencia
print("DataFrame")
df = pd.DataFrame([["Laptop", 1200, 10], ["Teléfono", 800, 25], ["Tablet", 300, 15], ["Monitor", 400, 20]], columns = ["Producto", "Precio", "Stock"])
print(df)
#a parir de una lista de diccionarios
print("DataFrame")
df = pd.DataFrame([{"Producto": "Laptop", "Precio": 1200, "Stock": 10}, {"Producto": "Teléfono", "Precio": 800, "Stock": 25}, {"Producto": "Tablet", "Precio": 300, "Stock": 15}, {"Producto": "Monitor", "Precio": 400, "Stock": 20}])
print(df)

