import pandas as pd

# Leer el archivo .xlsx
# Reemplaza la ruta con la ruta a tu archivo .xlsx
xlsx_file = r'C:\Users\garci\Videos\ISS.xlsx'  # Reemplaza con la ruta a tu archivo .xlsx
df = pd.read_excel(xlsx_file)

# Guardar el DataFrame como .csv
# Reemplaza la ruta con la ruta donde quieres guardar el archivo .csv
#reemplaza el nombre del archivo con el que quieras guardarlo
csv_file = r'C:\Users\garci\Documents\Python_2024'  # Reemplaza con la ruta donde quieres guardar el archivo .csv
df.to_csv('iss.csv', index=False)

print(f"Archivo convertido y guardado como {csv_file}")
