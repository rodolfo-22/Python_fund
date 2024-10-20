#vamos a leer archivos csv
import pandas as pd
#pon el r antes de la ruta para que no haya problemas con los slashes
#si te da problemas usa en encoding='latin-1'
df = pd.read_csv(r'C:\Users\garci\Documents\Python_2024\python_04\data1.csv')
print(df)