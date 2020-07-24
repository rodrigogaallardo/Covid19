!wget 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
archivo = pd.read_csv("full_data.csv")  # Leer el archivo csv
excel = archivo.to_dict("list")        # Lo convierto en un diccionario
# creo la variable pais, que es la que voy a iterar para encontrar el pais correspondiente
pais = (excel["location"])

x1 = []
x2 = []
y1 = []
y2 = []
a = 0
b = 0
c = 0
country = ""

def get_nacion():
    # Se pido al usuario que ingrese el pais
    country = str(input("ingrese nacion que desea buscar: "))
    # Como el diccionario los paises inician en Mayuscula, al primer caracter lo tranformo en mayuscula
    country = country[0].upper()+country[1:]

    # verifico que el pais ingresado se encuentre en el diccionario
    existe = False
    while existe == False:
        for i in pais:

            if (i == country):
                existe = True
                break
            else:
                existe = False

        if (existe == False):
            country = str(input("Pais no encontrado, vuelva a ingresarlo: "))
            country = country[0].upper()+country[1:]

    return country


country = get_nacion()

# Recorro el pais ingresado sobre "pais=excel["location"]"
for i in pais:
    # Utilizo un contador para saber en que indice comienza el pais seleccionado
    a += 1
    # En el reccorido voy comparando el pais con el contenido de la variable
    if (i == country):
        # Guardo el indice en cual inicia
        b = a
        # Con otro contador, acumulo las veces que itera
        c += 1

# Para poder extraer los valores de ["total_cases"] y ["date"].
# inicia en el indicie del pais seleccionado, hasta su ultima mención
for j in range(b-c, b):
    # Agrego los valores a x, y
    y1.append(excel["total_cases"][j])
    x1.append(excel["date"][j])

 # Mismo proceso para["total_deaths"]
for j in range(b-c, b): 
    y2.append(excel["total_deaths"][j])
    x2.append(excel["date"][j])

# Genero los graficas
plt.figure(figsize=(40, 10))  
plt.title(country)

plt.subplot(1, 2, 1)
plt.plot(x1, y1, "y-")
plt.xlabel('Dias transcurridos')
plt.ylabel('Cantidad de casos')
plt.xticks(rotation=45)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x2, y2, "r-")
plt.xlabel('Dias transcurridos')
plt.ylabel('Cantidad de fallecidos')
plt.grid()
plt.xticks(rotation=45)

plt.show()