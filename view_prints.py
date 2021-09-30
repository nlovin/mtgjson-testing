import json
import pandas as pd

with open('data/raw/AllPrintings.json', encoding="utf8") as f:
    data = json.load(f)

#print(data['data']['10E']['name'])
editions = data['data'].keys()
#cards = data['data']['10E']['cards'].keys()

for edition in editions:
    print(data['data'][edition]['name'])
    cards_n = len(data['data'][edition]['cards']))
    
    for i in cards_n:
        print(data['data'][edition]['name'][i]['name'])
    #print(data['data'][edition])
    break