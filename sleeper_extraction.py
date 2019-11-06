from sportsreference.nfl.boxscore import Boxscore
from sportsreference.nfl.roster import Player
from collections import defaultdict
import pprint
import sys
import json

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
                key,value = line.strip().split(': ')
                sleepers_2019[key].append(value)
            pp.pprint(sleepers_2019)
            with open('sleepers2019.json', 'w') as f:
                json.dump(sleepers_2019, f, indent=4)
        elif file == "SleeperList_2018.txt":
            for line in sleepers:
                key,value = line.strip().split(': ')
                sleepers_2018[key].append(value)
            pp.pprint(sleepers_2018)

