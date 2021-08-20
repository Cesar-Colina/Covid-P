#United States COVID-19 Cases and Deaths by State over Time database API
#
import json
import urllib.request, urllib.parse, urllib.error
import time
import sqlite3

#create a table to store all of the data
connect = sqlite3.connect('CovidStatsdb.sqlite')
cur = connect.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS Stats (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, state_id FLOAT, submission_date TEXT,
total_deaths FLOAT, new_deaths FLOAT, total_cases FLOAT, new_cases FLOAT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS States(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, population INTEGER)''')

url = 'https://data.cdc.gov/resource/9mfq-cb36.json'
# ?state=STATE&$order=submission_date
# link format to access the API and grab info for a specific date in order of every day since the pandemic

NewYork = dict()
iterate = dict()
states = ['NYC', 'CA', 'FL', 'TX', 'SD']

statestateNum = 1
# 1, 2, 3, 4, 5
# key values for the states


for state in states:

    cur.execute('''INSERT INTO States (name) VALUES (?)''', (state,))
    apiurl = url + '?state=' + state + '&$order=submission_date'
    #create the link for the approriate state

    print('accessing url: ' , apiurl)
    data = urllib.request.urlopen(apiurl)
    data = data.read().decode()
    print(len(data), ' characters retrieved')

    try:
        js = json.loads(data)
        print(len(js), ' length of list')
    except:
        js = None
    if not js:
        print("*****************failure to retrieve******************")
        #error message if data fails to load


    for count in range(len(js)):
        if js[count]['state'] == state:
            subd = js[count]['submission_date']
            totd = js[count]['tot_death']
            newd = js[count]['new_death']
            totc = js[count]['tot_cases']
            newc = js[count]['new_case']

            cur.execute('''INSERT INTO Stats (state_id, submission_date, total_deaths, new_deaths, total_cases, new_cases)
            VALUES (?, ?, ?, ?, ?, ?)''',(stateNum, subd, float(totd), float(newd), float(totc), float(newc), ))

    connect.commit()
    #commit after each state
    #import a time delay to avoid throttling
    time.sleep(1.5)
    stateNum = stateNum + 1
