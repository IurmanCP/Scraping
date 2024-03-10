import csv
import json
import sys
from getpass import _raw_input

import requests

import bs4
import pandas as pd
import time

variable = _raw_input('Que productos desea buscar? ');
#elemento = sys.argv[1]

print("Variable pasada: ", variable)

from bs4 import BeautifulSoup
#URL of the website to scrape
url = 'https://supermercado.laanonimaonline.com/almacen/aceites/girasol/n3_89/'
#page = requests.get(url)

#print(page.text)

# Send an HTTP GET request to the website
response = requests.get(url);

#Parse the HTML code using BeautifulSoup
soup = bs4.BeautifulSoup(response.content, 'html.parser')

#Stablish the csv file
csv_file = 'precios_aceites.csv'

scripts = soup.find_all('script')

#Open the csv file only for writing
with open(csv_file, 'w', newline='') as file:
    #Create a writer csv
    writer = csv.writer(file)
    for script in scripts:
        #Obtenenmo
        script_content = script.string
        if script_content and 'dataLayer.push' in script_content:
            # Eliminar los caracteres no deseados y extraer los datos como un diccionario
            data_start = script_content.find('{')
            data_end = script_content.rfind('}') + 1
            data_str = script_content[data_start:data_end]
            if "var dataObject = {" not in data_str:
                try:
                    data_dict = eval(data_str)

                    # Obtener la lista de impresiones
                    impressions = data_dict['ecommerce']['impressions']

                    # Iterar sobre las impresiones para obtener los nombres y precios de los aceites
                    for impression in impressions:
                        oil_name = impression['name']
                        oil_price = float(impression['price'])
                        writer.writerow([oil_name, oil_price])

                except SyntaxError:
                    print("Error: Sintaxis inválida en la cadena.")

#Extract the relevant information from de HTML code
#movies = []
#for row in soup.select('sc-b0691f29-0 jbYPfh cli-children'):
#    title = row.find('h3', class_='ipc-title__text').find('a').get_text()
#    movies.append([title])

#Store the information in a pandas dataframe
#df = pd.DataFrame(movies, columns=['title'])

# Add a delay
time.sleep(1)

# Export the data to a CSV file
#df.to_csv('laanonima.csv', index=False)
