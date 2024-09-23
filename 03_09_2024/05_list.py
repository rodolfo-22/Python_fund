#listas, pilas y colas
my_list = [10,2,3,4,6,5,7,8,9,1,1]
print(my_list)
print(len(my_list))

my_list.append(11)
print(my_list)

my_other_list = [35, 17.5, "rodolfo"]
print(my_other_list)
print(type(my_other_list))
#imprimir algun elemento de la lista
print(my_other_list[1])
print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list.count(35))#para ver cuantas veces se repite un elemento

#concatenacion
print(my_list + my_other_list)

#una lista es mutable
#para insertar un elemento en una lista
my_2_list = ["azul", "rojo", "verde","dfasdf","rojo"]
my_2_list.append("amarillo")
print(my_2_list)
my_2_list.insert(1,'fsdaf')
print(my_2_list)
my_2_list.remove("rojo") #elimina por elemento interno
print(my_2_list)

my_2_list.pop() #elimina el ultimo elemento de la lista, y nos devuelve ese valor
print(my_2_list)

print(my_2_list.pop(1)) #elimina el elemento en la posicion 1
print(my_2_list)

del my_2_list[2] #elimina el elemento en la posicion 2
print(my_2_list)

my_2_list[0] = "morado" #cambiar un elemento de la lista
my_2_list.reverse()
print(my_2_list) #invierte la lista

my_2_list.sort()
print(my_2_list) #ordena la lista





#lista
#my_string = "hello word"
#print(my_string)
#print(type(my_string))