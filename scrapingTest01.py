from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configura las opciones del navegador para que no muestre la ventana
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar en modo headless, sin interfaz gráfica

# Ubicación del driver de Chrome (descarga desde https://sites.google.com/a/chromium.org/chromedriver/downloads)
chrome_driver_path = 'D:/chromedriver.exe'

# Configura el servicio de Chrome
service = Service(chrome_driver_path)
service.start()

# Inicializa el navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL del supermercado que deseas raspar
url = 'https://supermercado.laanonimaonline.com/buscar?pag=1&clave=arrozclear'

# Carga la página
driver.get(url)

# Espera unos segundos para asegurarse de que la página se haya cargado completamente
time.sleep(5)

# Encuentra todos los contenedores de productos
product_containers = driver.find_elements(By.CLASS_NAME, 'vtex-product-summary-2-x-nameContainer')

# Lista para almacenar los nombres de los productos
product_names = []

# Itera sobre los contenedores y extrae los nombres de los productos
for container in product_containers:
    name_element = container.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-brandName')
    product_names.append(name_element.text.strip())

# Cierra el navegador
driver.quit()

# Imprime los nombres de los productos
for name in product_names:
    print(name)