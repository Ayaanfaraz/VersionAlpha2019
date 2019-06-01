
import re
from urllib import urlopen
stats = urlopen('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=1151FF2B5E80B68F9951145B6297FD2E&steamid=76561198230401688').read()

test = str(stats)
array = test.split('"');
index = array.index("total_kills")
valueIndex = index+3
total = array[valueIndex]
killtotal = str(total)
totalKills = str(re.findall('\d+', killtotal)[0])
print("Total Kills: ",  totalKills)
killInt = float(totalKills)

array2 = test.split('"');
index = array2.index("total_deaths")
valueIndex2 = index+3
total2 = array2[valueIndex2]
deathtotal = str(total2)
totalDeaths = str(re.findall('\d+', deathtotal)[0])
deathInt = float(totalDeaths)

print("Total Deaths: ",  totalDeaths)

print("K/D Ratio: ", killInt/deathInt)