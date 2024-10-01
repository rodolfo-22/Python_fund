#un menu
while True:
    seguir = input("1 para el menú, 0 para salir: ")
    
    if seguir == "1":
        print("Seleccione una opción:")
        print("1- para sumar")
        print("2- para restar")
        print("0- para salir")

        x = input("Elige una opción: ")

        if x == "1":
            print("Estamos sumando...")
        elif x == "2":
            print("Estamos restando...")
        elif x == "0":
            print("Regresando al menú principal...")
        else:
            print("Opción no válida, por favor elige 1, 2 o 0.")
        
    elif seguir == "0":
        print("Saliendo...")
        break  # Rompe el ciclo para salir
    
    else:
        print("Opción no válida, por favor elige 1 o 0.")