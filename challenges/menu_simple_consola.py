def mostrar_menu_principal():
    print("\n=== Menú Principal ===")
    print("1- Mostrar opciones del menú")
    print("0- Salir")
    return input("Elige una opción: ")

def mostrar_menu_opciones():
    print("\n=== Opciones ===")
    print("1- Sumar")
    print("2- Restar")
    print("0- Volver al menú principal")
    return input("Elige una opción: ")

def realizar_operacion(opcion):
    if opcion == "1":
        print("Estamos sumando...")
    elif opcion == "2":
        print("Estamos restando...")

def menu():
    while True:
        opcion_principal = mostrar_menu_principal()
        
        if opcion_principal == "1":
            while True:
                opcion_menu = mostrar_menu_opciones()
                
                if opcion_menu in ["1", "2"]:
                    realizar_operacion(opcion_menu)
                elif opcion_menu == "0":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, elige 1, 2 o 0.")
        
        elif opcion_principal == "0":
            print("Saliendo del programa...")
            break  # Sale del ciclo principal y finaliza el programa.
        else:
            print("Opción no válida. Por favor, elige 1 o 0.")
            
menu()
