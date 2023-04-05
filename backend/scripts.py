import requests
import config
from functools import lru_cache
import datetime
from html2image import Html2Image

@lru_cache()
def get_settings():
    return config.Settings()

hti = Html2Image()

getenv = config.Settings()

async def getSteamProfileData(id):
    data = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={getenv.steam_id}&steamids={id}")
    data = data.json()['response']['players'][0]
    return data

async def getSteamGamesData(id):
    data = requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={getenv.steam_id}&steamid={id}&format=json")
    data = data.json()['response']
    return data

async def htmlToImage(html):
    hti.screenshot(html_content=html, save_as=f"/test.png")

def convertTime(unix):
    return datetime.datetime.fromtimestamp(int(unix)).strftime('%d %B %Y %I:%M %p')
    

# get id --> get data --> render to html --> convert to image --> save to R2 bucket, with name same as the id --> return rhino image url

# Get achievements: https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=440&key=D0DDCE10E6EC149D4010D3C5795EEBC2&steamid=76561198386606986

# GetUserStatsForGame: http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=440&key=D0DDCE10E6EC149D4010D3C5795EEBC2&steamid=76561198386606986

# GetOwnedGames: http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=D0DDCE10E6EC149D4010D3C5795EEBC2&steamid=76561198386606986&format=json