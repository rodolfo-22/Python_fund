#set: tienen de base un array

my_set = set()
my_other_set = {}
print(type(my_set))

my_other_set = {24, 45.7, "hola",'canmbion', 24,"hola"}
print(my_other_set)

my_other_set.add("nuevo") #un set no es una estrucutra ordenada
print(my_other_set)
#un set no permite elementos duplicados
my_other_set.add("nuevo")
print(my_other_set)

print(len(my_other_set))
print("hola" in my_other_set)
my_other_set.clear()
print(my_other_set)
del my_other_set    #elimina la variable

my_set = {1,2,3,4,5}
my_other_set = {24, 45.7, "hola",'canmbion', 24,"hola"}

my_sum_set =my_set.union(my_other_set)
print(my_sum_set)
#print(my_other_set[2]) #no se puede acceder a los elementos de un set por indice





