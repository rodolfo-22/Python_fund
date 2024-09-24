#loops
#es una manera de repetir un bloque de codigo// bucles, ciclos

while True:
    print("Esto se imprime siempre")
    break   

my_condition = 0
while (my_condition < 10):
    print("es menor que 10")
    
    my_condition += 1
    print(my_condition)

while (my_condition < 10):
    print("es menor que 10")
else:
    print("es mayor que 10")

print("ejecutando el siguiente ")
my_condition = 0
while (my_condition < 10):
    my_condition += 2
    if my_condition == 6:
        print("es igual a 5")
    print("el numero va por: " + str(my_condition))

print("ejecutando el siguiente ")
my_condition = 0
while (my_condition < 10):
    my_condition += 2
    if my_condition == 6:
        print("es igual a 5")
        break
    print("el numero va por: " + str(my_condition))


#For
#itera sobre una secuencia de elementos
my_list = [1,2,3,4,5,6,7,8,9,10]
for item in my_list:
    print(item)

print("siguiente for")
for item in my_list:
    if item == 5:
        break
    print(item)