import requests
import pandas as pd
import json

league_id = 472351
season    = 2019
espn = "AECjevBWtskaSx2%2FHnUUvkJg3YfRKR5RJx1aVopdVjuD9GVoxtRKJD7YIh64umim0kX%2BAEVrhqeLY2Udtg4cBQEGV5imcgcwaFiEN4iq%2FHq7dTfad6RhJ2VeVUvcIArFBf0ezHkhzJ28xvE1HyZNxZ7475GqHNDhpqhpXL0KFXkFuLm1yt8iJBBcfiNFLpKwdUQYuVbtNAvK0f1lqqg%2Fvkw0zjH%2B69w2Tq1By%2BEXUDTMmyJ8dFte%2FXD%2BkJsP6vqF1xKsPK7Ujq1whNrI9jnUTqL3"
swid = "{C00B1776-4205-49F6-8B17-764205C9F6CB}"

slotcodes = {
    0 : 'QB', 2 : 'RB', 4 : 'WR',
    6 : 'TE', 16: 'Def', 17: 'K',
    20: 'Bench', 21: 'IR', 23: 'Flex'
}

url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/' + \
      str(season) + '/segments/0/leagues/' + str(league_id) + \
      '?view=mMatchup&view=mMatchupScore'

newData = {}
newData['players'] = []
print('Week ', end='')
for week in range(8, 9):
    print(week, end=' ')

    r = requests.get(url,
                     params={'scoringPeriodId': week},
                     cookies={"SWID": swid, "espn_s2": espn})
            
    d = r.json()

    print(json.dumps(r.json(),indent=4))
    
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


            newData['players'].append({
                name : {
                    'week' : week,
                    'postion' : slot,                
                    'stats' : {
                        'projected points' : proj,
                        'actual points' : act
                    }
                }
            })

            # data.append([
            #     week, tmid, 'name' : name, slot, pos, inj, proj, act
            # ])

            with open('data.json', 'w') as f:
                json.dump(newData, f, indent=4)

print('\nComplete.')

# data = pd.DataFrame(data, 
#                     columns=['Week', 'Team', 'Player', 'Slot', 
#                              'Pos', 'Status', 'Proj', 'Actual'])

#print(data.head())
