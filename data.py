import numpy as np 
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import unicodecsv as csv
import unidecode
import sys
import codecs





sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


# get the data from the website
url = 'https://worldathletics.org/records/toplists/sprints/100-metres/outdoor/men/senior/2023'
response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', attrs={'class':'records-table'})




rows = table.find_all('tr')[1:]


m_sprinters = []


for row in rows:
    cols = row.find_all('td')
    rank = cols[0].text.strip()
    mark = cols[1].text.strip()
    wind = cols[2].text.strip()
    name = cols[3].text.strip()
    nat = cols[5].text.strip()

    m_sprint = { 
    'rank': rank,
    'mark': mark,
    'wind': wind,
    'name': name,
    'nat': nat

}
    m_sprinters.append(m_sprint)
    print("Rank: ", rank)
    print("Mark: ", mark)
    print("Wind: ", wind)
    print("Name: ", name)

    print("Nat: ", nat)
    print("--------------------")




# creating the dataframe







df = pd.DataFrame(m_sprinters, columns=['rank', 'mark', 'wind', 'name', 'nat'])
print(df)

df.to_csv('100M_Male.csv', index=False)


## connect to sqlite3 database

import sqlite3

conn = sqlite3.connect('sprinters.db')

c = conn.cursor()

df.to_sql('sprinters', conn, if_exists='replace', index = False)

c.execute('''CREATE TABLE sprinters
                ([rank] INTEGER PRIMARY KEY, [mark] text, [wind] text, [name] text, [nat] text)''')
