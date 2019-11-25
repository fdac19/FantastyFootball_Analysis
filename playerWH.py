import json
import sys
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sportsreference.nfl.boxscore import Boxscore
from sportsreference.nfl.roster import Player
from collections import defaultdict
import pprint
import re

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

playerArr = []
fortyArr = []

sleepers_2019 = defaultdict(list) # dictionary with value as lists
sleepers_2018 = defaultdict(list) 

pp = pprint.PrettyPrinter(compact=True)

# process both files from commandline
# store the sleepers of 2019 and 2018 into resepctive dictionaries
file = sys.argv[2]
print("file being processed: %s " % file) 
with open(file,'r') as sleepers:
    if file == "SleeperList_2018.txt":
        for line in sleepers:
            key,value,player_id, forty = re.split(': |, ', line)

            #print(forty.strip('\r\n'))
            sleepers_2019[key].append(value)
                
            player = Player(str(player_id).rstrip()) # strip the trailing newline after getting player_id from txt file
            if player != None:
                if(key == slotSearch):
                    print("player: %-20s Height: %-10s Weight: %-3dlbs" %(value, player.height, player.weight)) 
                    print(forty)

                    playerArr.append(value)
                    fortyArr.append(forty.strip('\r\n'))

fortyArr = list(map(float,fortyArr))
print(fortyArr)

plt.barh(playerArr, fortyArr, align='center', alpha=0.5)
plt.xlabel('Time (sec)')
#plt.title('Player 40 Yard Dash Times')

# plt.show()
#plt.rcdefaults()
#fig, ax = plt.subplots()

# Example data
"""people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')"""

plt.show()