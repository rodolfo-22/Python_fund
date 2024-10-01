#calcule si es unnumero primo
x = int(input("Ingrese un número: "))
for i in range(2,x):
    if x % i == 0:
        print("No es primo")  
        break
    else:     
        print("Es primo")
        break