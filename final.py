
import re
from urllib import urlopen
stats = urlopen('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=1151FF2B5E80B68F9951145B6297FD2E&steamid=76561198230401688').read()


def getStat(statName):
    test = str(stats)
    array = test.split('"');
    index = array.index(statName)
    valueIndex = index + 3
    total = array[valueIndex]
    ktotal = str(total)
    totalC = str(re.findall('\d+', ktotal)[0])
    kI = float(totalC)
    return kI

kills = getStat("total_kills")
deaths = getStat("total_deaths")

print("Total Kills: ", int(kills))
print("Total Deaths: ", int(deaths))
print("K/D Ratio: ", float(kills/deaths))