!wget 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'

########################################################################################################

#La aplicación debe recibir del usuario el nombre del país deseado y graficar casos detectados 
#y fallecimientos totales para ese país en función del tiempo.

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

#########################################################################################################


fecha=(excel["date"])
x3=[]
x4=[]
y3=[]
y4=[]
x5=[]
y5=[]
x6=[]
y6=[]

a=0
d=0
b=0
e=0
c=0
f=0

print("Primer Pais")
country2=nacion()

print("Segundo Pais")
country3=nacion()

def fech_ing(a):

  dia=str(input("Ingrese dia : "))
  mes=str(input("Ingrese mes : "))
  año=str(input("Ingrese año : "))
  print(f"La fecha ingresada es: {dia} / {mes} / {año} ") 
  fecha=[año,mes,dia]
  sep="-"
  fecha_ver=sep.join(fecha)
 
  return fecha_ver 

#Utilizo la misma logica que realice en item 1 pero para ambos paises
for i in pais:                                                                                                                        
  a+=1
  if (i==country2):
    b=a
    c+=1

for i in pais:
  d+=1
  if (i==country3):
    e=d
    f+=1


#Se pide al usuario que ingrese la fecha incial y final
print("Ingreso de fecha inicial del intervalo (DD-MM-AAAA)")
inicio=fech_ing("")    

print("Ingreso de fecha final del intervalo (DD-MM-AAAA)") 
final=fech_ing("") 

#Verifico que exista la fecha para los paises seleccionados
#En caos de que no se encuentren datos para dichas fechas(inicio/final)
#Se le volvera a pedir al usuario que reingrese una fecha

existe=False
e_ini=False

while existe==False:

  for j in range(b-c,b):

    if(fecha[j]==inicio):
      print("existe inicio")
      e_ini=True

      for z in range(b-c,b):
        if (fecha[z]==final):
          print("existe final")
          existe=True

  if(existe==False):
    if e_ini==True:
       print("Para la fecha final del primer pais, no  se encuentran  datos")
       print("Vuelva a ingresar fecha final")
       final=fech_ing("")

    else:
       print("Para la fecha incial del primer pais, no  se encuentran  datos")
       print("Vuelva a ingresar fecha inicial")
       inicio=fech_ing("")
     

   

  
existe=False
e_ini=False

while existe==False:

  for j in range(e-f,e):

    if(fecha[j]==inicio):
      print("existe inicio")
      e_ini=True

      for z in range(e-f,e):
        if (fecha[z]==final):
          print("existe final")
          existe=True
          

  if(existe==False):
     if e_ini==True:
         print("Para la fecha final del segundo pais, no  se encuentran  datos")
         print("Vuelva a ingresar fecha inicial")
         inicio=fech_ing("")

     else:
        print("Para la fecha incial del segundo pais, no  se encuentran  datos")
        print("Vuelva a ingresar fecha final")
        final=fech_ing("")
     
     
#Realizo el mismo procedimiento del punto anterior para extraer los valores
# de X,Y para ["total_deaths"],["date"]    
# Aunque solo tomara los datos si cumple con la condicion, desde la fecha inicial
#-hasta el final, exluyendo el resto de los dias 
     
for j in range(b-c,b):                                                   
                                                                         
  if(fecha[j]>=inicio and fecha[j]<=final):                               
    y3.append(excel["total_deaths"][j])                                   
    x3.append(excel["date"][j])  

for j in range(e-f,e):
  
  if(fecha[j]>=inicio and fecha[j]<=final):
    y4.append(excel["total_deaths"][j])
    x4.append(excel["date"][j])
                                                                       
#Realizo el primer grafico
plt.figure(figsize=(40, 10))                                             
plt.subplot(1, 2, 2)
plt.plot(x3,y3, "b-",label=country2)
plt.plot (x4,y4,"g-",label=country3)
plt.xlabel('Dias transcurridos')
plt.ylabel('Cantidad de fallecidos')
plt.xticks(rotation=60)
plt.grid()

# Realizo el mismo procedimiento del punto anterior para extraer los valores
# de X,Y para ["total_cases"],["date"]
# Con la exclusion de los dias que no estan dentro del intervalo de tiempo ingresado

for j in range(b-c,b):
  
  if(fecha[j]>=inicio  and fecha[j]<=final  ):                          
    y5.append(excel["total_cases"][j])                                  
    x5.append(excel["date"][j])                                          

for j in range(e-f,e):
  
  if(fecha[j]>=inicio and fecha[j]<=final  ):
    y6.append(excel["total_cases"][j])
    x6.append(excel["date"][j])
                                                                        
#Realizo el segundo grafico
plt.subplot(1, 2, 1)                                                    
plt.plot(x5,y5,"b-",label=country2)
plt.plot(x6,y6,"g-",label=country3)
plt.xlabel('Dias transcurridos')
plt.ylabel('Cantidad de casos')
plt.title(country2+"--"+country3)
plt.xticks(rotation=60)

plt.legend()
plt.grid()
plt.show()

#######################################################

#Pedir al usuario ingresar n países y gráficar para dichos países la cantidad de casos en una escala logaritmica. 
#El programa debe pedirle al usuario el intervalo de tiempo

import numpy as np
import matplotlib.pyplot as plt

pais =excel["location"]
f=0
g=0
h=0
y7=0
x7=0
val=[]
archivo=[]

#Se le pide al usuario la cantidad de paises a ingresar
cantidad=int(input("Cuantos paises desea ingresar en el sistema: "))      
for i in range(0,cantidad):
  #lo cual generara un array en donde se guardaran los paises a usar 
  p=nacion()                                                                                                    
  archivo.append(p)

#Se pide al usuario que ingrese la fecha incial y final
print("Ingreso de fecha inicial del intervalo (DD-MM-AAAA)")
inicio=fech_ing("")    

print("Ingreso de fecha final del intervalo (DD-MM-AAAA)") 
final=fech_ing("")

#Se va a iterar sobre el array con los paises generados, lo cual 
#-van a ser buscado.
#Utilizo la misma logica que realice en los anteriores puntos
 #-pero para los paises deseados

for paises in archivo:                                                          
                                                                          
  for j in pais:                                                          
    f+=1                                                                 
    if (j==paises):
      g=f
      h+=1

  #Verifico que exista la fecha para los paises seleccionados
  #En caos de que no se encuentren datos para dichas fechas(inicio/final)
  #Se le volvera a pedir al usuario que reingrese una fecha

  existe=False
  e_ini=False

  while existe==False:

    for j in range(g-h,g):

      if(fecha[j]==inicio):
        print("existe inicio")
        e_ini=True

        for z in range(g-h,g):
          if (fecha[z]==final):
            print("existe final")
            existe=True

    if(existe==False):
      if e_ini==True:
       
        print(f"Para {paises} en la fecha final no  se encuentran  datos")
        print("Vuelva a ingresar fecha final")
        final=fech_ing("")   
      else:
        
        print(f"Para {paises} en la fecha incial no  se encuentran  datos")
        print("Vuelva a ingresar fecha inicial")
        inicio=fech_ing("")

     
      
       
#Realizo el mismo procedimiento del punto anterior para extraer los valores
#Aunque solo tomara los datos si cumple con la condicion, desde la fecha inicial
#-hasta el final, exluyendo el resto de los dias.
#Y los valores van a ser guardados en la variable VAL, que es con los valores['total_cases']
#-que vamos a realizar el grafico


  for j in range(g-h,g):                                                  

    if(fecha[j]>=inicio and fecha[j]<=final):                            
      val.append(excel['total_cases'][j])                                 
                                                                          
    plt.yscale('log')                                                     
    plt.plot(np.log(val), "b-")
                                                                          
#Realizo el logaritmo pero el problema que tuve en este punto fue que los valores
# de x e y, se me iban reemplazando por ende tuve que optar por mostrar los 
# la escala logaritmica de cada pais por separado

#Realizo el grafico de la escala logaritmitca de n pais:

  plt.title("Escala logaritmitca de: "+ paises)                                 
  plt.xticks(rotation=60)
  plt.xlabel('Dias transcurridos')
  plt.grid()
  plt.show()
  val=[]
  f=0
  g=0
  h=0

###########################################################################

#Almacenar en un archivo de excel los países ordenados de mayor cantidad de casos a menor cantidad de casos 
#-indicando en las distintas columnas la cantidad de casos y fallecimientos de cada país. 
#Colocar en distintas hojas del archivo excel la evolución de este ranking, 
#-es decir armar una hoja para cada día transcurrido (Defina los días a utilizar acorde a cuanta información 
#-se disponga, podría ser una entrada del programa).

from pandas import ExcelWriter
import itertools

archivo = pd.read_csv("full_data.csv") # Leer el archivo csv
date = archivo.date.unique()           # Elimino los dias repetidos
dateV=[]                               # Creo una variable en donde voy a guardar los dias junto con los datos

for i in date:
  dateV.append(archivo[(archivo.date==i)&(archivo.location!="World")].sort_values(by="total_cases", ascending=False))
#Dentro de este for recorro todos los dias, junto con el .sort ordeno de manera descendente 
# a los "total_cases". Y los guardo en la variable dateV
#Imrpimo la variable para ver si guardo lso datos correctamente
print(dateV)                                            
#Guardo los datos obtenidos en distintas hojas
with ExcelWriter("Covid_19_Dia_x_Dia.xlsx") as writer: 
  # esto lo logra gracias a iterar dateV 
  for i in dateV:                                       
    i.to_excel(writer, sheet_name=i.date.unique()[0])
