#using the information available on https://worldpopulationreview.com/states
import sqlite3
import urllib.request, urllib.parse, urllib.error
import bs4
import re

states = ['California', 'New York', 'Florida', 'Texas', 'South Dakota']

pop = urllib.request.urlopen('https://worldpopulationreview.com/states').read()
soup = bs4.BeautifulSoup(pop, 'html.parser')
# print(soup)

tags = soup('li')
for tag in tags:
    #print(tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Population: ', tag.get_text())
    print(re.findall('^Population: (\S)', tag.get_text()))
    for state in states:

        if re.findall('^Population:  (\S+)', tag.get_text()) == state:
            print(tag.get_text())
    #print('Attrs:', tag.attrs)
