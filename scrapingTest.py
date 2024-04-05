import requests
from bs4 import BeautifulSoup
import csv
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def scrape_supermarket(url):
    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup)

    # Encontrar todos los contenedores de productos
    product_containers = soup.find_all('div', class_='vtex-product-summary-2-x-nameContainer flex items-start')
    print("contenedor")
    print(product_containers)
    # Lista para almacenar los detalles de los productos
    product_details = []

    for container in product_containers:
        # Extraer el nombre del producto
        name = container.find('span', class_=re.compile(r'vtex-product-summary.*-productBrand')).text.strip()

        # Extraer el precio del producto
        price = container.find('div', class_=re.compile(r'veaargentina-store-theme.*')).text.strip()
        print("nombre")
        print(name)
        # Agregar el nombre y el precio a la lista de detalles del producto
        product_details.append({'Name': name, 'Price': price})

    # Ordenar la lista de detalles del producto por precio
    sorted_product_details = sorted(product_details, key=lambda x: float(
       x['Price'].replace('$', '').replace('.', '').replace(',', '.')))

    return sorted_product_details



def save_to_csv(product_details, filename):
    # Escribir los detalles de los productos en un archivo CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in product_details:
            writer.writerow(product)


# URL del supermercado que deseas raspar
url = 'https://www.vea.com.ar/coca%20cola?_q=coca%20cola&map=ft'

# Llamar a la función para raspar la página web
product_details = scrape_supermarket(url)

# Nombre del archivo CSV donde se guardarán los datos
csv_filename = 'productos_supermercado.csv'

# Guardar los detalles de los productos en un archivo CSV
save_to_csv(product_details, csv_filename)

