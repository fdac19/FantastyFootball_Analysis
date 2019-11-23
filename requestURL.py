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
                        'postion' : slot,                
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
