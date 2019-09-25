# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import re


browser = webdriver.Firefox(r"C:\Users\Reda\Documents\Code\Python")

url = 'https://data.startups.be/actors?actor_type=LegalEntity&limit=100'
browser.get(url)
browser.implicitly_wait(5) 
html = browser.page_source

soup = BeautifulSoup(html, 'lxml') 

#CLICK ON "SHOW 100 PAGE"
browser.maximize_window()
page = browser.find_element_by_xpath('/html/body/div/div[5]/div[2]/div/div/div[3]/div[3]/div[2]/div/ul/li[3]/div')
page.click()


i = 1
for i in range(1, 101):
    
    #ITERATE TOUGH ALL THE STARTUPS ON THE PAGE
    doc = browser.find_element_by_xpath('/html/body/div/div[5]/div[2]/div/div/div[3]/div[3]/div[1]/div/div/div['+ str(i) + ']/div/div[2]/div[3]')
    doc.click()
    html = browser.execute_script('return document.documentElement.outerHTML')
    sel_soup = BeautifulSoup(html, 'lxml')
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 100)")
    browser.implicitly_wait(20) 


    social = sel_soup.find('div', class_='side-panel__company-info__social-information')
    #GET CRUNCHBASE URL
    cb_url = re.findall(r'https://www.crunchbase.com/organization/[a-zA-Z0-9._-]+', html)
    print(cb_url)
    time.sleep(3)
    #DISMISS STARTUP AFTER CLICKING ON IT
    remove = browser.find_element_by_xpath('/html/body/div/div[5]/div[3]/div/div/div/div[1]/button')
    remove.click()
    time.sleep(3)
    

    


    
    
    