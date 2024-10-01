#funciones de orden superior son funciones que reciben como argumento otra funcion
# y/o devuelven una funcion
from functools import reduce

def suma_one(value):
    return value + 1

def suma_five(value):
    return value + 5

def sum_values (val1, val2, f_suma):
    return f_suma(val1 + val2)

print(sum_values(10, 20,suma_one)) #31
print(sum_values(10, 20,suma_five)) #35


###Closure
#son funciones que devuelven otra funcion
#la funcion devuelta tiene acceso a las variables locales de la funcion que la contiene
def sum_ten():
    def add_ten(value):
        return value + 10
    return add_ten

add_clousere = sum_ten()
print(add_clousere(10)) #20

#build-it higher order function
#son funciones que devuelven otra funcion
#la funcion devuelta es generada en tiempo de ejecucion
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,50,11,10]

def multy(num):
    return num * 2

print(list(map( multy ,numbers )))

print(list(map( lambda num: num * 2 ,numbers )))

print(list(filter(lambda num: num % 2 == 0, numbers)))

print(list(filter(lambda num: num > 10, numbers)))

#reduce

liss = [11,10]

def summ(a, b):
    return a + b

print(reduce(summ,liss))