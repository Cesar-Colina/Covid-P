#using the information available on https://worldpopulationreview.com/states
import sqlite3
import urllib.request, urllib.parse, urllib.error
import bs4
import re

states = ['California', 'New York', 'Florida', 'Texas', 'South Dakota']
populations = dict()

popurl = urllib.request.urlopen('https://worldpopulationreview.com/states').read()
soup = bs4.BeautifulSoup(popurl, 'html.parser')


tags = soup('li')
#grab the population from the desired states
for tag in tags:

    for state in states:
        if re.findall('^\S+', tag.get_text())[0] == state or \
        re.findall('^\S+.\S+', tag.get_text())[0] == state:
            #find the states and put the popluation value in a dictionary
            try:
                people = re.findall('[0-9]+,[0-9]+,[0-9]+', tag.get_text())[0]
                #more than 6 digits
            except:
                people = re.findall('[0-9]+,[0-9]+', tag.get_text())[0]
                #6 digits or less

            # remove the comma's and store as an integer
            tempL = people.split(',')
            storage = ''
            for index in range(len(tempL)):
                storage = storage + tempL[index]

            populations[state] = populations.get(state, int(storage))

print(populations)

#upload them into the database
connect = sqlite3.connect('CovidStatsdb.sqlite')
cur = connect.cursor()

cur.execute('UPDATE States SET population= ? WHERE id=1', (populations['New York'], ))
cur.execute('UPDATE States SET population= ? WHERE id=2', (populations['California'], ))
cur.execute('UPDATE States SET population= ? WHERE id=3', (populations['Florida'], ))
cur.execute('UPDATE States SET population= ? WHERE id=4', (populations['Texas'], ))
cur.execute('UPDATE States SET population= ? WHERE id=5', (populations['South Dakota'], ))
connect.commit()
