# Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos
#  e imprimir por pantalla
ciudades = ["Alcobendas", "Reus", "Orense", "Gerona", "Baracaldo", "Alcorcón", "San Fernando",
            "San Cugat del Vallés", "Manresa", "Pontevedra", "Cáceres", "Torrevieja", "Coslada", 
            "El Puerto de Santa María", "Santiago de Compostela", "Majadahonda", "Vélez-Málaga", 
            "Ibiza", "Zamora", "Pamplona", "Fuengirola", "Benidorm", "Villareal", "Villalba"]

print(type(ciudades))
#Imprimir por pantalla el segundo elemento de la lista
print(ciudades[1])
#Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:4])
# Visualizar todos los elementos de la lista a partir del tercero de manera genérica,
print(ciudades[2:])
#Visualizar los primeros 4 elementos de la lista
print(ciudades[:3])
#Agregar otra ciudad, pero en la cuarta posición
print("insertar ciudades")
ciudades.insert(3, "city1")
print(ciudades)
#Concatenar otra lista a la ya creada
new_list = ["city2", "city3"]
total_city = ciudades + new_list
print(total_city)
#¿Qué pasa si se busca un elemento que no existe?
#print(ciudades[30]) #list index out of range
#Eliminar un elemento de la lista
ciudades.remove("Alcobendas")
print(ciudades)
#¿Qué pasa si el elemento a eliminar no existe?
#ciudades.remove("Alcobendas") #ValueError: list.remove(x): x not in list
#Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
print(total_city)
last_city = total_city.pop()
print(last_city)
#Mostrar la lista multiplicada por 4
list_mult = ["alabama","arka"]
print(list_mult * 4)


#tuplas, no se pueden modificar
# Crear una tupla que contenga los números enteros del 1 al 20
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20)
#Imprimir desde el índice 10 al 15 de la tupla
print(tupla[9:15])
#Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in tupla)
print(30 in tupla)
# Con la lista creada en el punto 1, validar la existencia del elemento 'París' 
# y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.""
existe = "París" in ciudades
print(existe)
if not existe:
    ciudades.append("París")
    print("se agrego paris a la lista de ciudades")
    print(ciudades)
else:
    print("paris ya existe en la lista, por lo tanto no se agrego")
#Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la 
# tupla y de la lista
print(tupla.count(20))
print(ciudades.count("París"))
#Convertir la tupla en una lista
tupla_list = list(tupla)
print(tupla_list)
#Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

#Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". 
# Agregar tambien otras claves, como puede ser "Pais" y "Continente".
# Imprimir las claves del diccionario
# Imprimir las ciudades a través de su clave