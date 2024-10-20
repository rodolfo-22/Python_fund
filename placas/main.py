#uso de dataframes
import pandas as pd
#df = pd.read_csv(r'C:\Users\garci\Documents\Python_2024\placas_corregidas.csv')
#print(df)

# Abrir el archivo para lectura
with open(r'C:\Users\garci\Documents\Python_2024\placas_corregidas.csv', 'r',encoding='latin-1') as f:
    # Leer todas las líneas
    lines = f.readlines()

# Obtener el número de columnas esperado (de la primera línea)
num_cols = len(lines[0].split(','))  # Cambia el delimitador si es otro

# Lista para almacenar las líneas corregidas
corrected_lines = []

# Corregir las líneas que tienen más columnas
for i, line in enumerate(lines):
    # Dividir la línea por el delimitador
    cols = line.split(',')
    
    # Si tiene más columnas que las esperadas, reducirla a las primeras num_cols
    if len(cols) > num_cols:
        print(f"Corrigiendo la línea {i+1}: {len(cols)} columnas encontradas, ajustando a {num_cols}")
        # Tomar solo las primeras num_cols columnas
        corrected_lines.append(','.join(cols[:num_cols]) + '\n')
    else:
        # Mantener la línea sin cambios si está correcta
        corrected_lines.append(line)

# Escribir el archivo corregido
with open('placas_corregidas.csv', 'w') as f:
    f.writelines(corrected_lines)

print("Archivo corregido y guardado como 'placas_corregidas.csv'.")
