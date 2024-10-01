#gestor de paquetes para python
#pip install
#pit --version
#instalamos numpy, sirve para trabajar con arrays
import numpy as np
print(np.__version__)

np_array = np.array([1,2,3,4,5])
print(type(np_array))

print(np_array * 2)

#pandas, sirve para trabajar con dataframes
import pandas as pd


#request
import requests
#consumamos la pokeapi
respuesta = requests.get('https://pokeapi.co/api/v2/pokemon?limit=11')
print(respuesta.status_code)
print(respuesta.json())


#paquete desde archivo .py
# paquete desde ini.py
import mypackage
print(mypackage.add(2,3))
print(mypackage.multiply(2,33))