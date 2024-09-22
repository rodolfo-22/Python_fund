my_string = "Hello, World!"
print(my_string)
print(my_string, my_string)
print(len(my_string))

my_new_line_string = "estr es un string\ncon un salto\\nde linea"
print(my_new_line_string )
lanzar_tabulacion = "esto es un string\tcon una tabulacion"
print(lanzar_tabulacion)

#como formatear los strings
print("hola, mi nombre es %s y tengo %d años" % ("Juan", 30)) #tal cual imprima el objeto
name = "pedro"
age = 50
print("mi nombre es {} y {}".format(name, age))   

#inferencia de datos
print(f"mi nombre es {name} y tengo {age} años") 

#desenpaquetado de caracteres
languajes = "python"
a,b,c,d,e,f = languajes
print(c)
print(d)

languaje_slice = languajes[0:6:2]
print(languaje_slice)

#metodos o funciones del sistema
print(languajes.capitalize()) #primera en mayuscula
print(languajes.upper()) #todo en mayuscula
print(languajes.lower()) #todo en minuscula
print(languajes.replace("p", "j")) #reemplazar caracteres
print(languajes.split("t")) #separar caracteres
print(languajes.count("t")) #contar caracteres
print(languajes.find("t")) #buscar caracteres
print(languajes.index("t")) #buscar caracteres
print(languajes.isnumeric()) #verificar si es numerico
print(languajes.isalpha()) #verificar si es alfanumerico
print(languajes.isalnum()) #verificar si es alfanumerico
print(languajes.islower()) #verificar si es minuscula
print(languajes.isupper()) #verificar si es mayuscula
print(languajes.isspace()) #verificar si es espacio
print(languajes.istitle()) #verificar si es titulo
print(languajes.endswith("n")) #verificar si termina con un caracter
print(languajes.startswith("p")) #verificar si inicia con un caracter
print(languajes.strip()) #quitar espacios en blanco
print(languajes.lstrip()) #quitar espacios en blanco a la izquierda
print(languajes.rstrip()) #quitar espacios en blanco a la derecha
print(languajes.center(10)) #centrar el texto
print(languajes.ljust(10)) #justificar a la izquierda
print(languajes.rjust(10)) #justificar a la derecha
print(languajes.zfill(10)) #rellenar con ceros
print(languajes.title()) #poner en titulo
print(languajes.swapcase()) #cambiar mayusculas por minusculas y viceversa
print(languajes.partition("t")) #partir el string
print(languajes.rpartition("t")) #partir el string
print(languajes.join("t")) #unir string
print(languajes.encode()) #codificar string
print(languajes.expandtabs()) #expandir tabulaciones
print(languajes.format()) #formatear string
print(languajes.format_map("t")) #formatear string
print(languajes.rfind("t")) #buscar caracter









