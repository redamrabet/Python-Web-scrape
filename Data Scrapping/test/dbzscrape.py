from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://jean-oikonomou.github.io/PORTOFOLIO/').text
soup = BeautifulSoup(source, 'lxml')

# csv_file = open('jean_scrape.csv', 'w')

# csv_writer = csv.writer(csv_file)

# csv_writer.writerow(['description', 'link'])

match = soup.find('img')['src']
print(match)  
print()

match2 = soup.find('div', class_='squareContent')
a = match2.h2.text
a2 = match2.h3.text
print(a)
print()

print(a2)
print()

for match3 in soup.find_all('div', class_='skill ml-3'):
    try:
        para = match3.p.text
        h4 = match3.h4.text
        percent = match3.span.text

        print(percent)
        print(h4) 
        print(para)

    except expression as identifier:
        pass

print()

for match5 in soup.find_all('div', class_='squareContent'):
    try:
        count = match5.h2.text
        stats = match5.h3.text

        print(count)
        print(stats)
        print()

    except expression as identifier:
        pass

for match6 in soup.find_all('div', class_='icons'):
    try:

        description = match6.a.get('data-caption')
        link = match6.a.findNext('a').get('href')

        print(description)
        print(link)
       
        print()

        # csv_writer.writerow([description, link])

    except expression as identifier:
        pass
        
        
    
linkk = soup.find('a', class_='gitlink')['href']

get_jean = linkk.split('/')[3]

print(get_jean)

# csv_file.close() 


    



         
 
   
