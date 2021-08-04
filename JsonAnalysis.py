#United States COVID-19 Cases and Deaths by State over Time database API
import json
import urllib.request, urllib.parse, urllib.error

apiurl = 'https://data.cdc.gov/resource/9mfq-cb36.json'

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

NewYork = dict()


for count in range(1000):
    #print(js[count]['state'])
    if js[count]['state'] == 'NYC':
        #print(count, " hi")
        #print(js[count]['submission_date'])
        NewYork[js[count]['submission_date']] = NewYork.get(js[count]['submission_date'], js[count]['tot_cases'])

print(NewYork)

#print(js)
#print(json.dumps(js, indent = 4))
