#diccionarios, almacenan datos en pares clave:valor

my_dicc = {}
my_other_dicc = dict()

my_other_dicc = {"nombre":"Juan", "apellido":"Perez", "edad":24}

my_dicc = {
    "nombre":"Juan",
    "nombre":"Pedro",
    "apellido":"Perez",
    "edad":24,
    "lenguajes" : {"python","swift","java"}
}

print(my_dicc)
print(len(my_dicc))

print(my_dicc["nombre"])
print(my_dicc["lenguajes"])

del my_dicc["nombre"]
print(my_dicc) 

print("apellido" in my_dicc)

print(my_dicc.keys())
print(my_dicc.values())
print(my_dicc.items())

my_new_dicc = dict.fromkeys(my_dicc)
print(my_new_dicc)

my_new_dicc = dict.fromkeys(my_dicc, "Comentario") #asigna un valor a todas las claves
