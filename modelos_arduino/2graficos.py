import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
archivo_csv = 'datos_relevantes.csv'
datos = pd.read_csv(archivo_csv, header=None, names=["Tiempo (ms)", "Motor", "Distancia (cm)"])

# Filtrar los datos por ejes
datos_x = datos[datos["Motor"] == "X"]
datos_y = datos[datos["Motor"] == "Y"]
datos_z = datos[datos["Motor"] == "Z"]

# Crear gráficos
def graficar_eje(datos, eje):
    plt.figure(figsize=(10, 6))
    plt.plot(datos["Tiempo (ms)"], datos["Distancia (cm)"], marker='o', linestyle='-', label=f"Eje {eje}")
    plt.title(f"Desplazamiento en el eje {eje}")
    plt.xlabel("Tiempo (ms)")
    plt.ylabel("Distancia (cm)")
    plt.grid(True)
    plt.legend()
    plt.show()

# Graficar eje X
if not datos_x.empty:
    graficar_eje(datos_x, "X")

# Graficar eje Y
if not datos_y.empty:
    graficar_eje(datos_y, "Y")

# Graficar eje Z
if not datos_z.empty:
    graficar_eje(datos_z, "Z")

