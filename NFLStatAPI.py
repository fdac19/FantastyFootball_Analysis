from sportsreference.nfl.boxscore import Boxscore
from sportsreference.nfl.roster import Player

sleepersTest = ['McCaCh01']

ChristianM = Player('McCaCh01')
print(ChristianM.name)  # Prints 'Drew Brees'
print(ChristianM.passing_yards)  # Prints Brees' career passing yards
print(ChristianM.birth_date)
print(ChristianM.height)
print(ChristianM.weight)

for currSleeper in sleepersTest: 
    print(currSleeper)
    # currPlayer = Player(currSleeper)
    # playerName = currPlayer.name
    # playerHeight = currPlayer.height
    # playerWeight = currPlayer.weight

    # print(currPlayer.name)


