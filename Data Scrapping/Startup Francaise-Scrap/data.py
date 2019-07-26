# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import csv

mainsource = requests.get('https://www.myfrenchstartup.com/fr/dernieres-levees-de-fonds-des-startups-francaises').text
soup = BeautifulSoup(mainsource, 'lxml')

# csv_file = open('first-scrap.csv', 'w')

# csv_writer = csv.writer(csv_file)

# csv_writer.writerow(['Startup', 'Ville', 'Montant', 'Date', 'Investisseurs', 'Nombre'])

# csv_writer.writerow(['Fondateur', 'Description'])

table = soup.find('table', class_='table text-nowrap')
tbody = table.find('tbody')

for tr in tbody.find_all('tr'):
    startup = tr.find_all('div', class_='media-left')[1].find_all('a')[0].text
    ville = tr.find_all('div', class_='media-left')[1].find_all('div')[1].text.strip()
    montant = tr.find_all('td')[1].text.strip()
    date = tr.find_all('td')[2].text.strip()
    investisseurs = tr.find_all('td')[3].text.strip()
    nombre = tr.find_all('td')[4].text.strip()
    # print(startup, ville, montant, date, investisseurs, nombre)

    url = tr.find_all('div', class_='media-left')[1].find_all('a')[0]['href']
    subsource = requests.get(url).text
    subsoup = BeautifulSoup(subsource, 'lxml')
    
    col = subsoup.find('div', class_='col-lg-9')
    panel = col.find('div', class_='panel-body')

    # print(panel)  
    fondateur = [fondateur.getText() for panel in panel.find_all('p', class_='content-group') for fondateur in panel.find_next_siblings('b')]
    description = [description.getText() for panel in panel.find_all('p', class_='content-group') for description in panel.find_next_siblings('p')]
    print(fondateur, description)
    print()
   


#     csv_writer.writerow([fondateur, description])


