#comprimida de listas

my_original_list = [1,2,3,4,5,6,7,8,9,10]
print(my_original_list)

my_rang =range(8)
print(list(my_rang))

my_list = [ i for i in range(1,11)]
print(my_list)

my_list = [ i*2 for i in range(8)]
print(my_list)

my_list = [ i*i for i in range(8)]
print(my_list)
#es una lista que se modifica al momento de ser creada

def sum_five (number):
    return number + 5

my_list = [ sum_five(i) for i in range(8)]
print(my_list)










