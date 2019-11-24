import requests
import pandas as pd
import json

league_id = 472351
season    = 2019


slotcodes = {
    0 : 'QB', 2 : 'RB', 4 : 'WR',
    6 : 'TE', 16: 'Def', 17: 'K',
    20: 'Bench', 21: 'IR', 23: 'Flex'
}

swid = "{C00B1776-4205-49F6-8B17-764205C9F6CB}"
espn = "AEA9UNNKGrEtSmioOr2m7LaT%2BoWEAEGojR21xEfCpwC9b5XJDJZCjEPA8AIkT28tM%2BDzjp4Tj5%2FOmQrOK%2B%2FvqQmpIBKMg88ZjQKTVRzRPicGr43lbp0festA9wx9it5f3n6RRGF5%2FaIWOzS3UpZNg%2FEC2Tl6%2FfIZJWyM0UAxQ9I44Mu4eOpi78KEcBtVG7P9%2Bly9gWrR5YKxoB%2FR1xnCc3jYJiT9U2KCz9xmz6gNit02WaMzX5lsr0Ej9xVoCPBoxRyN%2BZ96F%2B1WKieUBd2L8ar2B0BxDb6cl%2BDCJyKsp5VWWw%3D%3D"

url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/' + \
      str(season) + '/segments/0/leagues/' + str(league_id) + \
      '?view=mMatchup&view=mMatchupScore'

newData = {}
print('Week ', end='')
for week in range(6, 9):
    print(week, end=' ')

    r = requests.get(url,
                     params={'scoringPeriodId': week},
                     cookies={"SWID": swid, "espn_s2": espn})
            
    d = r.json()
    
    for tm in d['teams']:
        tmid = tm['id']
        for p in tm['roster']['entries']:
            name = p['playerPoolEntry']['player']['fullName']
            slot = p['lineupSlotId']
            pos  = slotcodes[slot]

            # injured status (need try/exc bc of D/ST)
            inj = 'NA'
            try:
                inj = p['playerPoolEntry']['player']['injuryStatus']
            except:
                pass

            # projected/actual points
            proj, act = None, None
            for stat in p['playerPoolEntry']['player']['stats']:
                if stat['scoringPeriodId'] != week:
                    continue
                if stat['statSourceId'] == 0:
                    act = stat['appliedTotal']
                elif stat['statSourceId'] == 1:
                    proj = stat['appliedTotal']

            if name in newData:
                newData[name]['stats'].append({
                        'week' : week,
                        'projected points' : proj,
                        'actual points' : act
                    })
            else:
                newData[name] = {
                        'position' : slot,                
                        'stats' : [{
                            'week' : week,
                            'projected points' : proj,
                            'actual points' : act
                        }]
                }

            with open('data.json', 'w') as f:
                json.dump(newData, f, indent=4)

print('\nComplete.')

# data = pd.DataFrame(data, 
#                     columns=['Week', 'Team', 'Player', 'Slot', 
#                              'Pos', 'Status', 'Proj', 'Actual'])

#print(data.head())
