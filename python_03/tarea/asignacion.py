#Tareas: Completa los siguientes pasos usando pandas. Asegúrate de documentar tu código para que sea claro y comprensible.
import pandas as pd 
#Crea una Serie llamada precios con los precios de cierre de las acciones de las 
# siguientes empresas: "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA". Usa estos precios: 
# 175.50, 2850.30, 310.20, 3555.72, 799.90.

#Define los índices de la Serie con los nombres de las acciones de las empresas
precios = pd.Series([175.50, 2850.30, 310.20, 3555.72, 799.90], index=["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"])
print(precios)

#Imprime los índices y valores de la Serie precios.
print(precios.index)
print(precios.values)
print(type(precios))

#Calcula el precio promedio de las acciones utilizando la Serie precios
print("El precio promedio de las acciones es: ", precios.mean())
#Muestra el valor máximo y mínimo de la Serie y las empresas correspondientes.
print("El maximo valor es ", precios.max(), "y corresponde a" ,precios.idxmax())
print("El minimo es",precios.min(),"y corresponde a ", precios.idxmin())

#Aplica una función que incremente el precio de cada acción en un 2% y 
# guarda el resultado en una nueva Serie llamada precios_actualizados.
precios_actualizados = precios.apply(lambda x: x*1.02)
print("Precios actualizados: ", precios_actualizados)
#Redondea los valores de precios_actualizados a dos decimales.
precios_actualizados = precios_actualizados.round(2)
print("Precios actualizados redondeados: ", precios_actualizados)

#Filtra precios para mostrar solo las acciones con un precio superior a 500.
print("Precios mayores a 500: ", precios[precios > 500])
#Filtra precios_actualizados para mostrar solo las acciones que tienen un 
#precio actualizado entre 200 y 800
print("Precios actualizados entre 200 y 800: ", precios_actualizados[(precios_actualizados > 200) & (precios_actualizados < 800)])

#Ordena la Serie precios en orden descendente.
precios_ordenados = precios.sort_values(ascending=False)
print("Precios ordenados de mayor a menor:\n ", precios_ordenados)
#Ordena la Serie precios_actualizados en orden ascendente y muestra los primeros tres elementos.
precios_actualizados_ordenados = precios_actualizados.sort_values()
print("Precios actualizados ordenados de menor a mayor:\n ", precios_actualizados_ordenados.head(3))

#Crea una Serie llamada rendimiento, que calcule el porcentaje de rendimiento 
# de cada acción en relación con su precio original. Usa la siguiente fórmula:
#rendimiento = ((precios_actualizados - precios) / precios) * 100
rendimiento = ((precios_actualizados - precios) / precios) * 100
print("Rendimiento de las acciones:\n ", rendimiento)
#Calcula el porcentaje de cambio entre los precios originales y los precios 
# actualizados para cada acción. ¿Qué empresa muestra el mayor cambio?
print("Empresa con mayor cambio porcentual: ", rendimiento.idxmax(), "con un cambio de ", rendimiento.max(), "%")
#Identifica qué acciones tienen un rendimiento superior al 15%. ¿Cuántas acciones cumplen con este criterio?
rendimiento_superior = rendimiento[rendimiento > 15]
print("Acciones con rendimiento superior al 15%: ", rendimiento_superior)
#Crea una clasificación para las acciones basada en su rendimiento: "Alto" 
# si el rendimiento es mayor al 10%, "Medio" si es entre 5% y 10%, y "Bajo" 
# si es menor al 5%.
print("Clasificación de rendimiento:")
print(rendimiento.apply(lambda x: "Alto" if x > 10 else "Medio" if x > 5 else "Bajo"))


