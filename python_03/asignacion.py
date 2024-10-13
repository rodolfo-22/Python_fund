#crear serie de precios de acciones
import pandas as pd
precios = pd.Series([100, 200, 150, 900, 850], index = ["AAPL", "GOOGL", "AMZN", "MSFT", "FB"])
print(precios)

#Explorar atributos de la serie
print(precios.index)
print(precios.values)
print(type(precios))

#Calcular estaisticas descripitivas
#calcular el precio promedio
promedio = precios.mean()
print(promedio)
#mostrar el maximo y minimo junto con su indice
print(precios.idxmax())
print(precios.max())
print(precios.idxmin())
print(precios.min())

#Aplicar una funcion a la serie
precios_actualizados = precios.apply(lambda x: x * 1.2)
print("precios actualizados")
print(precios_actualizados)

#filtrar datos en la serie
print("Mostrar los precios mayores a 500")
print(precios[precios>500])
print("Mostrar los precios entre 200 y 700")
print(precios[(precios_actualizados > 200) & (precios_actualizados < 700)])

#Ordenar la serie orden deseendente
print("Ordenar la serie en orden descendente")
print(precios.sort_values(ascending=False))
#ordenar asendente pero que muestre los primeros 3 elementos
print("Ordenar la serie en orden ascendente")
print(precios.sort_values().head(3))

#clcualr el rendimiento de las acciones
rendimiento = ((precios_actualizados - precios) / precios) * 100
print("Rendimiento de las acciones")
print(rendimiento)
print("Rendimiento promedio")
print(rendimiento.mean())
print(rendimiento.max())
print(rendimiento.idxmax())
print(rendimiento.min())
print(rendimiento.idxmin())
#rendimiento mayor al 15%
print("Rendimiento mayor al 15%")
print(rendimiento[rendimiento > 15]) 
print("clasificacion por rendimento")
print("rend alto :")
print(rendimiento[rendimiento > 15].index)
print("rend medio :")
print(rendimiento[(rendimiento > 5) & (rendimiento < 15)].index)
print("rend bajo :")
print(rendimiento[rendimiento < 5].index)

# Definir los límites y las etiquetas para clasificar los valores
bins = [0, 300, 600, float('inf')]  # Rango: 0-300, 300-600, 600+
labels = ['Bajo', 'Medio', 'Alto']
# Clasificar la serie según los límites y etiquetas
clasificaciones = pd.cut(precios, bins=bins, labels=labels)
print(clasificaciones)
#examples

#https://colab.research.google.com/drive/1YxPYMAg6o-UiV22HNZa7_1pjp5YHXQi5#scrollTo=JFr8-OyquZQz
