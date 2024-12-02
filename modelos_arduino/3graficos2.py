import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
archivo_csv = 'datitos2.csv'
datos = pd.read_csv(archivo_csv, header=None, names=["Tiempo (ms)", "Motor", "Distancia (cm)"])

# Filtrar los datos por ejes
datos_x = datos[datos["Motor"] == "X"]
datos_y = datos[datos["Motor"] == "Y"]
datos_z = datos[datos["Motor"] == "Z"]

# Crear gráficos sin modificar las distancias
def graficar_eje(datos, eje):
    plt.figure(figsize=(10, 6))
    plt.plot(datos["Tiempo (ms)"], datos["Distancia (cm)"], marker='o', linestyle='-', label=f"Eje {eje}")
    plt.title(f"Desplazamiento en el eje {eje}")
    plt.xlabel("Tiempo (ms)")
    plt.ylabel("Distancia (cm)")
    plt.grid(True)
    plt.legend()
    plt.show()

# Menú para elegir el eje
while True:
    print("\nElige un eje para graficar:")
    print("1. Eje X")
    print("2. Eje Y")
    print("3. Eje Z")
    print("4. Salir")
    opcion = input("Ingresa el número de tu opción: ")

    if opcion == "1" and not datos_x.empty:
        graficar_eje(datos_x, "X")
    elif opcion == "2" and not datos_y.empty:
        graficar_eje(datos_y, "Y")
    elif opcion == "3" and not datos_z.empty:
        graficar_eje(datos_z, "Z")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida o no hay datos para el eje seleccionado.")
