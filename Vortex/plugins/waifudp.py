import asyncio
import os
import random
import re
import urllib
import requests
from telethon.tl import functions

from Vortex import CMD_HELP

COLLECTION_STRING = [
    "cute-anime-wallpapers-hd",
    "anime-christmas-wallpaper-hd",
    "anime-samurai-girl-wallpaper",
    "4k-anime-wallpapers",
    "2560-x-1440-wallpaper-anime",
]


async def waifupp():

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    plist = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(plist)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/Kanekiken44/VortexUB/raw/master/Extras/Vortex.ttf",
            "f.ttf",
        )

    r = requests.get(fy, allow_redirects=True)
    open('Vortexautopic.jpg', 'wb').write(r.content)


@Vortex.on(admin_cmd(pattern="waifupfp"))
async def main(event):

    await event.edit(
        "**Starting Automatic Waifu Profile Pic**.\n`Please Note That It Will Automatically Update Your Profile Pic After 10 Minutes`\nBy Your [VortexUB](https://github.com/kanekiken44/VortexUB)"
    )

    while True:

        await waifupp()
        file = await event.client.upload_file("Vortexautopic.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Vortexautopic.jpg")
        await asyncio.sleep(600)


CMD_HELP.update(
    {"waifudp": "➟ `.waifupic`\nRandomly Selects A Waifu Pic And Sets As Your Profile Picture.."}
)
