import json
import sys
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt

class position(Enum):
    QB = 0
    RB = 2
    WR = 4
    TE = 6

#Sleepers list of players by position
f = open('sleepers2019.json')
data = json.load(f)
f.close()

#All players in the NFL stats week by week
d = open('data.json')
fantasyPointData = json.load(d)
d.close

#Options: QB, RB, TE, WR, ALL
desiredPosition = sys.argv[1]

slotSearch = 'ALL'

if desiredPosition == 'QB':
    slotSearch = 'QuarterBack'
if desiredPosition == 'RB':
    slotSearch = 'RunningBack'
if desiredPosition == 'WR':
    slotSearch = 'WideReciever'
if desiredPosition == 'TE':
    slotSearch = 'TightEnd'

for pos, player in data.items():
    sleeperListLength = len(player)
    print(pos)

    if(pos == slotSearch or slotSearch == 'ALL'):
        for i in range(sleeperListLength):
            if player[i] in fantasyPointData:
                currPlayer = fantasyPointData.get(player[i])
                print(player[i])
                statsLength = len(currPlayer['stats'])
 
                for x in range(statsLength):
                    playerProjectedPoints = currPlayer['stats'][x]['projected points']
                    playerActualPoints = currPlayer['stats'][x]['actual points']
                    weekProj = currPlayer['stats'][x]['week']

                    plt.plot(weekProj, playerProjectedPoints)


plt.show()