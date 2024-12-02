import pandas as pd
import re

# Cambia 'archivo.csv' por la ruta de tu archivo CSV
csv_file = 'placas_corregidas.csv'
excel_file = 'placas_excel.xlsx'


# Leer el archivo CSV con encoding latin1 y evitar problemas de memoria
df = pd.read_csv(csv_file, encoding='latin1', low_memory=False)

# Función para eliminar caracteres ilegales
def clean_illegal_chars(value):
    if isinstance(value, str):
        # Solo elimina caracteres que no son imprimibles ni visibles
        return re.sub(r'[^\x20-\x7E\n]', '', value)
    return value

# Aplicar limpieza a todos los valores del DataFrame
df = df.applymap(clean_illegal_chars)

# Guardar como archivo Excel
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f"El archivo ha sido convertido a {excel_file} exitosamente.")
