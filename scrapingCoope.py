import csv
import json
import sys
from getpass import _raw_input

import requests

import bs4
import pandas as pd
import time
import re

#variable = _raw_input('Que productos desea buscar? ');
#elemento = sys.argv[1]

pagina = _raw_input("Por favor ingrese la pagina de la que desea ver los precios: ")
print("pagina ----> "+str(pagina))

#print("Variable pasada: ", variable)

#URL of the website to scrape
url = 'https://supermercado.laanonimaonline.com/panificados/n2_71/pag/3/'
#page = requests.get(url)

#check if another page exists
#La anonima has this page
pagina_extra = pagina + "pag/2/"

#Send a request to the page to check if exists
more_pages = requests.get(pagina_extra)
resp_more_pages = bs4.BeautifulSoup(more_pages.content, 'html.parser')

#print(resp_more_pages)
if 'mantenimiento' in resp_more_pages:
    print("La pagina esta en mantenimiento")
#print(pagina_extra)
#print(more_pages)


#establish the number of pages
cant_paginas = 1
if 'pag' in pagina:
    print("La url tiene mas de una pagina")
    #we add each page to know how many there are
    #this can be done a simpler way
    cant_paginas = cant_paginas + 1

#print(page.text)
print("cantidad de paginas")
print(cant_paginas)
# Send an HTTP GET request to the website
response = requests.get(url);

#Parse the HTML code using BeautifulSoup
soup = bs4.BeautifulSoup(response.content, 'html.parser')

#Stablish the csv file
#csv_file = 'precios_aceites.csv'

#scripts = soup.find_all('script')

#Open the csv file only for writing

#Extract the relevant information from de HTML code
#movies = []
#for row in soup.select('sc-b0691f29-0 jbYPfh cli-children'):
#    title = row.find('h3', class_='ipc-title__text').find('a').get_text()
#    movies.append([title])

productos = soup.find_all('div', class_='col1_listado')
prod = soup.select('col1_listado')
print("productos ----> ")
print(prod)


# Iterar sobre los elementos encontrados y extraer el texto de cada uno
for elemento_a in prod:
    nombre_producto = elemento_a.get_text()
    print(nombre_producto)

with open('productos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Precio'])
    for producto in productos:
        nombre = producto.text.strip()
        precio = producto.find_next_sibling('div', class_='precio').text.strip()

        # Eliminar símbolo de moneda y espacios en blanco
        precio = precio.replace('$', '').replace(',', '').strip()

        # Escribir los datos en el archivo CSV
        writer.writerow([nombre, precio])

#Store the information in a pandas dataframe
#df = pd.DataFrame(movies, columns=['title'])

# Add a delay
time.sleep(1)

# Export the data to a CSV file
#df.to_csv('laanonima.csv', index=False)
