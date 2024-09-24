#clases en python
#es una plantilla para crear objetos

class Person:
    pass   #pass es una palabra reservada que se usa para cuando no se quiere hacer nada

class MyPerson:
    #def y self son palabras reservadas, define el constructor de la clase
    def __init__(self, name, age, alias=""):
        self.name = name
        self.age = age
        self.alias = (alias)

    def walk(self):
        print(f"{self.name} is walking")

my_person = MyPerson("Juan", 30)
print(my_person.name)
my_person.walk()

my_other_person = MyPerson("Pedro", 25, "Pepito")
print(my_other_person.alias)

