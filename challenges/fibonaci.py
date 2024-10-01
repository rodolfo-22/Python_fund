"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""
#iterar al final es recorrer una lista de elementos
def fibonaci():
    var1 = 0
    var2 = 1
    for i in range(1,51):
        print(var1)
        fib = var1 + var2
        var1 = var2
        var2 = fib

fibonaci()