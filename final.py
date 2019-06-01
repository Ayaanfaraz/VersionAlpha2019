
import re # imports the reg ex library to find the information from the JSON string

def urlString(apiKEY, steamID): # create the definition for a string with a steam key and id passed in
    return 'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key='+apiKEY+'&steamid='+steamID

apiK = "1151FF2B5E80B68F9951145B6297FD2E" # steam api key
steamI = "76561198230401688" # steam id

from urllib import urlopen # call the url and parse the JSON into an array
stats = urlopen(urlString(apiK, steamI)).read()


def getStat(statName, stats): # gets the desired stat by passing in the name of the stat desired as well as the stat url
    test = str(stats)
    array = test.split('"');
    index = array.index(statName)
    valueIndex = index + 3
    total = array[valueIndex]
    stattotal = str(total)
    totalC = str(re.findall('\d+', stattotal)[0])
    finalTotal = float(totalC)
    return finalTotal

kills = getStat("total_kills", stats) # store each stat in a similarly named variable
deaths = getStat("total_deaths", stats)
totalContribution = getStat("total_contribution_score", stats)
KD = float(kills/deaths)

print("K/D Ratio: ", KD)
print("Contribution Score: ", int(totalContribution))

f= open(str(steamI),"a") #open a file for appending
f.write(str(KD))
f.write(" ")
f.write(str(totalContribution))
f.write("\n\n")
f.close();