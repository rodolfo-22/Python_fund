# Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir 
# por pantalla si es mayor o menor a cero
var1= 5.1
if var1 > 0:
    print("El número es mayor a cero.")
else:
    print("El número es negativo.")

#Crear dos variables y un condicional que informe si son del mismo tipo de dato
var2 = 5.124
if type(var1) == type(var2):
    print("Las variables son del mismo tipo de dato.")
else:
    print("Las variables son de distinto tipo de dato.")

# Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es par.")
    else:
        print(f"{i} es impar.")

#En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(6):
    print(f"{i} elevado a la potencia 3 es igual a {i**3}.")

#Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
var4 = 5
for i in range(var4):
    print(f"Este es el ciclo número {i+1}.")

#Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, 
# sólo si la variable contiene un número entero mayor a 0
#num1 = int(input("Ingrese un numero "))
num1 = 5
factorial = 1
if num1 > 0:
    while num1 > 0:
        factorial *= num1
        num1 -= 1
    print(f"El factorial es {factorial}.")

#Crear un ciclo for dentro de un ciclo while
var = 1
while var > 0:
    for i in range(0,5):
        print(i)
    break

varr = 0
while varr < 3:
    for i in range(0,2):
        print(i)
    varr += 1
    print("fin del ciclo del while")

#Crear un ciclo while dentro de un ciclo for
cont = 0
for i in range(0,2):
    while cont < 5:
        cont += 1 
        print(f"el numero de iteracion del while es {cont}")
    cont = 0
    print("dentro del while")

#Imprimir los números primos existentes entre 0 y 30
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo,", n, "es divisor")
            return False
    print(num, " es primo")
    return True

for i in range(2,31):
    es_primo(i)

#divisible entre 12
contt = 100
while contt <= 300:
    if contt % 12 == 0:
        print (contt,"es divisible entre 12")
    contt += 1

#Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la 
#opción al usario de buscar el siguiente
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo",)
            return False
    print("Es primo")
    return True
    
while True:
    opcion = input("ingrese un numero para saber si es primo o 0 para salir: ")
    
    if opcion > "0":
        es_primo(int(opcion))
        
    if opcion == "0":
        break

#Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

i = 100
while i <= 300:
    if i % 3 == 0 and i%6 == 0 :
        print(i, "es divisible")
        break
    i += 1
