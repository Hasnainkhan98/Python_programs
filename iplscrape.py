import requests
import json
import pandas as pd
import csv


url = 'https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/60-toprunsscorers.js?callback=ontoprunsscorers'
results = []
response = requests.get(url)
json_data = json.loads(response.text[response.text.find('(')+1:response.text.find(')')])

csv_file = open('iplt20_scarpe.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Player','Mat','Inns','NO','Runs','HS','AVG','BF','SR','100','50','4s','6s'])

for player in json_data['toprunsscorers']:
    data = {
        'Player': player['StrikerName'],
        'Mat': player['Matches'],
        'Inns': player['Innings'],
        'NO': player['NotOuts'],
        'Runs': player['TotalRuns'],
        'HS': player['HighestScore'],
        'AVG': player['BattingAverage'],
        'BF': player['Balls'],
        'SR': player['StrikeRate'],
        '100': player['Centuries'],
        '50': player['FiftyPlusRuns'],
        '4s': player['Fours'],
        '6s': player['Sixes']
    }
    results.append(data)
df = pd.DataFrame(results)
print(df)

csv_writer.writerow([results])

#Matches,Inns,NO,RUNS,HS,AVG,BF,SR,Hundreds,Fifty,Fours,Sixes

csv_file.close()