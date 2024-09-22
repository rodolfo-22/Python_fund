import math

#Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
my_variable =10
print(my_variable)

#Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

#Imprimir el tipo de dato de la variable creada en el punto 1
print(type(my_variable))

#Crear una variable que contenga tu nombre
my_name = "GOD"

#Crear una variable que contenga un número complejo
complejo = 3 + 4j
print(complejo)

#crea una varible que contenga el valor del numero pi, utilizando round(_,4) four decimal
print(round(math.pi,4))
print(f"{math.pi:.6f}")

#Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable = "true"
print(variable)
variable_2 = True
print(variable_2)

#Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(variable), type(variable_2))

# Asignar a una variable, la suma de un número entero y otro decimal
var_num = 5+5.5
print(var_num)
print(type(var_num))

# Realizar una operación de suma de números complejos
z1 = 3 + 4j
z2 = 2 + 5j
suma = z1 + z2
print(suma)

#Realizar una operación de suma de un número real y otro complejo
z3 = 5 
suma2 = z1 + z3
print(suma2)

# Realizar una operación de multiplicación
ent1 = 5
ent2 = 10
mult = ent1 * ent2
print(mult)
#Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
#cociente = 27//4 muestra solo el cociente, no el residuo
cociente = 27/4
print(cociente)

#De la división anterior solamente mostrar la parte entera
parte_entera = int(cociente)
print(parte_entera)

#De la división de 27 entre 4 mostrar solamente el resto
modulo = 27%4
print(modulo)

#Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
parte_entera_res = parte_entera * 4 + modulo
print(parte_entera_res )

#Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print("5jsdfhjsdafl" + "8sjjfjfjlsa")

#Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2) #comparacon, nos devuelve un boleano

#Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2") == 2)

#¿Por qué arroja error el siguiente cambio de tipo de datos?  por la coma
a = float('3.8')
print(a)

#Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
#  y que de como resultado 2.
val1 = 3
print(val1)
val1 -= 1
print(val1)

#Realizar la operacion 1 << 2 ¿Por qué da ese resultado? 
# ¿Qué es el sistema de numeración binario?
print(1 << 3)
#el de la izqui lo pasamos a binario y desplazamos el numero de posiciones del de la derecha 1000 1*2**3
#Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del 
# mismo tipo, siempre arrojaría el mismo resultado?
#print('2' + 2) #solo se pueden concatenar string, no enteros
print(2 + 2) #realiza la operacion
print('2' + '2') # los trata com estring y solo los cocatena, los une
# Realizar una operación válida entre valores de tipo entero y string
print( 5 + int('15'))
print( str(5)+ ' es un nuemro' )