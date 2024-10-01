#lamdas, son funciones anonimas que se pueden usar para simplificar el codigo
# fun anonimas, son las que no tienen nombre
# se usan para funciones sencillas
# se definen con la palabra reservada lambda
# lambda argumentos: expresion

sum = lambda val1, val2: val1 + val2

print(sum(10, 20)) #30

multi_values = lambda val1, val2, val3: val1 * val2 * val3
print(multi_values(2, 3, 4)) #24