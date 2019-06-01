
from urllib import urlopen
stats = urlopen('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=1151FF2B5E80B68F9951145B6297FD2E&steamid=76561198230401688').read()
print(stats)





