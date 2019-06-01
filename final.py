
import re

def urlString(apiKEY, steamID):
    return 'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key='+apiKEY+'&steamid='+steamID

apiK = "1151FF2B5E80B68F9951145B6297FD2E"
steamI = "76561198230401688"

from urllib import urlopen
stats = urlopen(urlString(apiK, steamI)).read()


def getStat(statName, stats):
    test = str(stats)
    array = test.split('"');
    index = array.index(statName)
    valueIndex = index + 3
    total = array[valueIndex]
    stattotal = str(total)
    totalC = str(re.findall('\d+', stattotal)[0])
    finalTotal = float(totalC)
    return finalTotal

kills = getStat("total_kills", stats)
deaths = getStat("total_deaths", stats)
totalContribution = getStat("total_contribution_score", stats)

#print("Total Kills: ", int(kills))
#print("Total Deaths: ", int(deaths))

print("K/D Ratio: ", float(kills/deaths))
print("Contribution Score: ", int(totalContribution))

f= open("initial.txt","w+")