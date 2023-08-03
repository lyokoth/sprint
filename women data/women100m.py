import bs4 as bs
import requests
import pandas as pd

url = 'https://worldathletics.org/records/toplists/sprints/100-metres/outdoor/women/senior/2023'
response = requests.get(url)
html_content = response.content

soup = bs.BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', attrs={'class': 'records-table'})

rows = table.find_all('tr')[1:]

w_100 = []  # Move the list initialization inside the loop

for row in rows:
    cols = row.find_all('td')
    rank = cols[0].text.strip()
    mark = cols[1].text.strip()
    wind = cols[2].text.strip()
    name = cols[3].text.strip()
    nat = cols[5].text.strip()
    date = cols[9].text.strip()

    w_100m = {
        'rank': rank,
        'mark': mark,
        'wind': wind,
        'name': name,
        'nat': nat,
        'date': date
    }

    w_100.append(w_100m)

df = pd.DataFrame(w_100, columns=['rank', 'mark', 'wind', 'name', 'nat', 'date'])
df['date'] = pd.to_datetime(df['date'], format='%d %b %Y')
print(df)

df.to_csv('100W.csv', index=False)