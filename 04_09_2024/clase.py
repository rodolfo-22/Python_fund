#Operadores adritmeticos, de comparaacion, logicos y de asigancion

print("3+5")
print(3+5)
print(10/2)
#modulo, devuelve el residuo de la division
print(10%3)

#operadores logicos
print(3>5)
paso =(3>5) and (4<6)
print(paso)

x =5
print(x)
x += 3
print(x)

#las sentencias condicionales se utilizan para tomar decisiones
num = 5
if num > 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")

#elif se utiliza para evaluar varias condiciones
temperature = 25  
if temperature < 0:  
    print("¡Hace frío!")  
elif temperature >= 0 and temperature < 15:  
    print("Hace frío.")  
elif temperature >= 15 and temperature < 25:  
    print("Es templado.")  
else:  
    print("Hace calor.")  

#bucle for, se utiliza para recorrer una secuencia de elementos
fruits = ["manzana", "banana", "cereza"]
for fruit in fruits:
	print(fruit)

#bucle while, se ejecuta mientras la condicion sea verdadera

count = 0  
while count < 5:  
    print("Cuenta:", count)  
    count += 1

#break, se utiliza para salir de un bucle de forma prematura
numbers = [1, 2, 3, 4, 5, 6]  
for number in numbers:  
    if number == 4:  
        break  
    print(number)  
#continue, se utiliza para saltar a la siguiente iteracion del bucle
#con impares
print("impares")
numbers = [1, 2, 3, 4, 5, 6]  
for number in numbers:  
    if number % 2 == 0:  
        continue  
    print(number)  

print("pares")
for number in numbers:  
    if number % 2 != 0:  
        continue  
    print(number)

#funciones
sss = input("ingrese su nombre: ")
def greet(nombre):
    print("Hola, " + nombre)  

greet(sss)

# Crear una variable que contenga un elemento del 
# conjunto de números enteros y luego imprimir por 
# pantalla si es mayor o menor a cero
x = 5
if x > 0:
    print("El número es mayor a cero.")
else:
    print("El número es negativo.")

#Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
# Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
#encontrar si un numero es primo
condicion = 1
while condicion == 1:
    condicion = int(input("Ingrese 1 para continuar o 0 para salir: "))
    num= int(input("ingresa un numero: "))
    valor= range(2,num)
    contador = 0
    for n in valor:
        if num % n == 0:
            contador +=1
    if contador > 0 :
        print("El número no es primo" )
    else:
        print("El nÚmero es primo")

#