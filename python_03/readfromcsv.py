# Paso adicional al usar Google Colab
from google.colab import drive
drive.mount('/content/drive')
path = '/content/drive/MyDrive/colesterol.csv'

import pandas as pd
df = pd.read_csv(path,sep=';')
df

df = pd.read_csv(path,sep=';', decimal = ',')
df

df.tail()

df.head()