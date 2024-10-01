#expresiones regulares
#comprobar si una cadena contiene un número
#nos dice s i lo tiene y nos devuelve todas las ocurrencias
"""
Las expresiones regulares (o regex) son patrones utilizados para buscar, validar o manipular
cadenas de texto. Son muy poderosas y se usan en muchos lenguajes de programación para realizar 
tareas como:
Búsqueda: Encontrar todas las ocurrencias de un patrón en un texto.
Validación: Verificar si una cadena de texto cumple con un formato específico (por ejemplo, una dirección de correo electrónico).
Sustitución: Reemplazar partes de una cadena de texto que coinciden con un patrón específico.
Extracción: Extraer partes específicas de una cadena de texto.
"""
import re

my_string = "Esta es la leccin numero 7, Expresiones regulares Leccion"
my_other_string = "Esta no es la leccion numero 7, Expresiones regulares"
print(re.match("Esta es la leccion", my_string))
print(re.match("Esta es la leccion", my_other_string))

match = print(re.match("Esta es la leccion", my_string))
#if match /= None:
if not match:
    print("El texto no coincide")

#utilizadno search
buscar = re.search("numero 7", my_string)
print(buscar)

#findall
btodo = re.findall("numero", my_string, re.IGNORECASE)
print(btodo)

#split
split = re.split(",", my_string)
print(split)

#sub
sub = re.sub("7", "8", my_string)
print(sub)
print(re.sub("leccion|Leccion", "LECCION", my_string))


#patrones
#los patrones se definen con el metodo compile
pattern = r"[l|L]eccion"
print(re.findall(pattern, my_string))

pattern = r"[l|L]eccion|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]+"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"[l]*"
print(re.findall(pattern, my_string))

#email validation regular expression
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
my_email = "mosfdfa@mosfo.com"
print(re.match(pattern, my_email))
print(re.search(pattern, my_email))
print(re.findall(pattern, my_email))

#par aprender y validar expresiones regulares https://regex101.com/