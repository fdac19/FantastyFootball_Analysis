import json
import sys

#Sleepers list of players by position
f = open('sleepers2019.json')
data = json.load(f)
f.close()

#All players in the NFL stats week by week
d = open('data.json')
fantasyPointData = json.load(d)
d.close

#Options: QB, RB, TE, WR, DEF
desiredPosition = sys.argv[1]

for pos, player in data.items():
    sleeperListLength = len(player)
    print(pos)

    for i in range(sleeperListLength):
        if player[i] in fantasyPointData:
            currPlayer = fantasyPointData.get(player[i])
            statsLength = len(currPlayer['stats'])

            for x in range(statsLength):
                playerProjectedPoints = currPlayer['stats'][x]['projected points']
                playerActualPoints = currPlayer['stats'][x]['actual points']
                weekProj = currPlayer['stats'][x]['week']
                print(playerActualPoints)
