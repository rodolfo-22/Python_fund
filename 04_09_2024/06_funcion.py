#Funciones

def my_funtion ():
    print("Hello from a function")

my_funtion()

def sumar(a,b):
    return a+b

print(sumar(2,3))
#a = input("Ingrese un numero: ")
#b = input("Ingrese otro numero: ")
#print(sumar(int(a),int(b)))

def print_name(name, surname):
    print(f"Hello {name} {surname}")    #f es para formatear la cadena, accede  a los valores de la variables

print_name("Juan", "Perez")

def print_name_default(name, lastname, areas="sin areas"):
    print(f"Hello {name} {lastname}, you are a {areas}")

print_name_default("Juan", "Perez", "Developer")

#pasandole mas de un parametro
def last_funtion(*text):
    print(text)

last_funtion("Hello", "World", "Python")

def print_parameters(*texts):
    for element in texts:
        print(element.upper())

print_parameters("Hello", "World", "Python")