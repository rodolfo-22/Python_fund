##Errores

#nameerror, ocurre cuando no se ha definido una variable
#print(name)

#index error, es cuando se intenta acceder a un indice que no existe
#list index out of range
lista = ["pyton","car","kotlin"]
#print(lista[4])
print(lista[2])

#ModuleNotFoundError, ocurre cuando se intenta importar un modulo que no existe
#import noexiste
import math
print(math.sqrt(1))

#AtributteError, ocurre cuando se intenta acceder a un atributo que no existe
#print(math.PI)
print(math.pi)

#KeyError, ocurre cuando se intenta acceder a una clave que no existe
my_dict = {"name":"carlos","age":25}
#print(my_dict["lastname"])
print(my_dict["name"])

#TypeError, ocurre cuando se intenta realizar una operacion con tipos de datos incorrectos
#print("5"+ 5)
#print(lista("2"))
print("5" + str(5))

#ImportError, ocurre cuando se intenta importar un modulo que no existe
#from math import PI 
from math import pi
import math
print(math.sqrt(1))

#ValueError, ocurre cuando se intenta realizar una operacion con un valor incorrecto
#int("hola")
int("2")

#ZeroDivisionError, ocurre cuando se intenta dividir por cero
#5/0
5/2