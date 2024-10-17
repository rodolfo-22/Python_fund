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




