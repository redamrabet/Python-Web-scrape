# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd




browser = webdriver.Firefox(r"C:\Users\Reda\Documents\Code\Python")
browser.get('https://www.myfrenchstartup.com/fr/connexion')
browser.maximize_window()


#LOGIN
acc = browser.find_element_by_name('login_connect')
acc.send_keys('testnotrobot8@gmail.com')
time.sleep(3)
pwd = browser.find_element_by_name('pwd')
pwd.send_keys('iamnotarobot')
time.sleep(5)
acc.send_keys(Keys.ENTER)

url = 'https://www.myfrenchstartup.com/fr/recherche-avancee'
browser.get(url)
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')


with open('myfrenchstartup.csv', 'a', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    i = 3
    for i in range(3, 13):
        


        html = browser.execute_script('return document.documentElement.outerHTML')
        sel_soup = BeautifulSoup(html, 'lxml')
        col = sel_soup.find('div', class_='col-lg-8')
        ul = col.find('ul', id='milieu')

        #Scraper
        for media in ul.find_all('div', class_='media-body'):
            #PAGE 1
            cname = media.find('h6').text.strip()
            cdiv = media.find('div').text.strip()
            ctype = media.find('p').text.strip()
            #print(cname, cdiv, ctype)
            #print()
        
            #PAGE 2
            url = media.find_all('a')[0]['href']
            browser.get(url)
            time.sleep(5)
            html = browser.page_source
            subsoup = BeautifulSoup(html, 'lxml')

            col = subsoup.find('div', class_='col-lg-9')
            panel = col.find('div', class_='panel-body')
  
            fondateur = [fondateur.getText() for panel in panel.find_all('p', class_='content-group') for fondateur in panel.find_next_siblings('b')]
            description = [description.getText() for panel in panel.find_all('p', class_='content-group') for description in panel.find_next_siblings('p')]
            #print(fondateur, description)
            #print()
       

            col = subsoup.find('div', class_='col-lg-3')
            thumb = col.find('div', class_='thumbnail')
            ul = thumb.find('ul')


            site = thumb.find('h6').text.strip()
            #print(site)
            #print()
        

            for link in ul.find_all('a', href=True):
                link = link['href']
                link = [link]
                #print(link)
                #print()
    

            tbody = col.find('tbody')
            for tr in tbody.find_all('tr'):
                try:
                    info = tr.find('td', class_='text-left').text
                    #print(info)
                    #print()
    
                except Exception:
                    pass

            writer.writerow([cname, cdiv, ctype, fondateur, description, site, link, info])


        url = 'https://www.myfrenchstartup.com/fr/recherche-avancee'
        browser.get(url)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    
        nextPage = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div/ul[2]/li[' + str(i) + ']/a')
        print(i)
        nextPage.click()
        time.sleep(5)

df = pd.read_csv('myfrenchstartup.csv')
df = df.drop_duplicates()
df.to_csv('noduplicates.csv', index=False)

df = pd.read_csv('noduplicates.csv')
df = df.drop_duplicates()
df.to_csv('noduplicates.csv', index=False)

browser.close()
csvfile.close()






    


