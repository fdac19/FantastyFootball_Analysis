import json
import sys
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

weekArr = []
projArr = []
actArr = []


for pos, player in data.items():
    sleeperListLength = len(player)
    palette = plt.get_cmap('Set1')
 
    #FOR PARTICULAR POSITION
    if(pos == slotSearch or slotSearch == 'ALL'):
        #FOR PARTICULAR PLAYER
        for i in range(sleeperListLength):
            projDF = pd.DataFrame([])
            if player[i] in fantasyPointData:
                currPlayer = fantasyPointData.get(player[i])
                print(player[i])
                statsLength = len(currPlayer['stats'])
 
                for x in range(statsLength):
                    playerProjectedPoints = currPlayer['stats'][x]['projected points']
                    playerActualPoints = currPlayer['stats'][x]['actual points']
                    weekProj = currPlayer['stats'][x]['week']

                    weekArr.append(weekProj)
                    projArr.append(playerProjectedPoints)
                    actArr.append(playerActualPoints)
                    #print(len(projDF))

                    #print(playerProjectedPoints)
                    print(weekProj)

                plt.plot(weekArr, projArr, '-go', color=palette(i), label=player[i])
                plt.plot(weekArr, actArr, '-go', color=palette(i), label=player[i])


                weekArr.clear()
                projArr.clear()
                actArr.clear()


#plt.plot(weekArr, projArr)
#plt.plot(projDF)

ax = plt.subplot(111)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
ax.set_xlabel('Week')
ax.set_ylabel('Projected Points')
ax.set_title(slotSearch + ' Player Projected Points')
plt.show()