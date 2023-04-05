from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import scripts
from jinja2 import Environment, FileSystemLoader
from html2image import Html2Image

app = FastAPI()

env = Environment(
    loader=FileSystemLoader("./"),
)

hti = Html2Image()

@app.get("/")
async def root():
    id = "76561198386606986"

    data = await scripts.getSteamProfileData(id)
    gameData = await scripts.getSteamGamesData(id)

    template = env.get_template("index.html")
    htmlData = template.render(name=data["realname"], id=data['personaname'], avatar=data['avatarfull'], url=data['profileurl'], games_owned=gameData['game_count'], last_online=scripts.convertTime(data['lastlogoff']))
    print(type(htmlData))

    hti.screenshot(html_str=htmlData, save_as="test.png")
    return HTMLResponse(htmlData)


@app.get("/data")
async def data():
    id = "76561198386606986"
    data = await scripts.getSteamProfileData(id)
    gameData = await scripts.getSteamGamesData(id)
    return {
        "profile": data,
        "games": gameData
    }