from sportsreference.nfl.boxscore import Boxscore
from sportsreference.nfl.roster import Player
from collections import defaultdict
import pprint
import sys
import json
import re

sleepers_2019 = defaultdict(list) # dictionary with value as lists
sleepers_2018 = defaultdict(list) 

pp = pprint.PrettyPrinter(compact=True)

# process both files from commandline
# store the sleepers of 2019 and 2018 into resepctive dictionaries
for file in sys.argv[1:]: 
    print("file being processed: %s " % file) 
    with open(file,'r') as sleepers:
        if file == "SleeperList_2019.txt":
            for line in sleepers:
                key,value,player_id = re.split(': |, ', line)
                sleepers_2019[key].append(value)
                
                player = Player(str(player_id).rstrip()) # strip the trailing newline after getting player_id from txt file
                if player != None:
                   print("player: %-20s Height: %-10s Weight: %-3dlbs" %(value, player.height, player.weight)) 

            #pp.pprint(sleepers_2019)
            with open('sleepers2019.json', 'w') as f:
                json.dump(sleepers_2019, f, indent=4)

        elif file == "SleeperList_2018.txt":
            for line in sleepers:
                key,value,player_id = re.split(': |, ', line)
                sleepers_2018[key].append(value)
            pp.pprint(sleepers_2018)
            with open('sleepers2018.json', 'w') as f:
                json.dump(sleepers_2018, f, indent=4)

