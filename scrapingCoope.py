import requests

import bs4
import pandas as pd
import time

#URL of the website to scrape
url = 'https://www.coopehogar.coop/'
page = requests.get(url)

print(page.text)

# Send an HTTP GET request to the website
response = requests.get(url);

#Parse the HTML code using BeautifulSoup
soup = bs4.BeautifulSoup(response.content, 'html.parser')

#Extract the relevant information from de HTML code
movies = []
for row in soup.select('sc-b0691f29-0 jbYPfh cli-children'):
    title = row.find('h3', class_='ipc-title__text').find('a').get_text()
    movies.append([title])

#Store the information in a pandas dataframe
df = pd.DataFrame(movies, columns=['title'])

# Add a delay
time.sleep(1)

# Export the data to a CSV file
df.to_csv('top-rated-movies.csv', index=False)
