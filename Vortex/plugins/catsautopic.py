import asyncio
import os
import random
import re
import urllib
import requests
from telethon.tl import functions
from Vortex import CMD_HELP

COLLECTION_STRING = [
    "cool-cat-wallpaper",
    "1920x1080-cat-wallpaper",
    "cat-wallpapers-and-screensavers",
    "baby-cat-wallpaper",
    "funny-cat-desktop-wallpaper",
]


async def meowrizoel():


    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    plist = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(plist)
    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/kanekiken44/VortexUB/raw/master/Vortex/resources/vortex.ttf",
            "f.ttf",
        )
    r = requests.get(fy, allow_redirects=True)
    open('vortexautopic.jpg', 'wb').write(r.content)


@Vortex.on(admin_cmd(pattern="meowpfp"))
async def main(event):

    await event.edit(
        "**Starting Automatic Cats Profile Pic**.\n`Please Note That It Will Automatically Update Your Profile Pic After 10 Minutes`\nBy [VortexUB](t.me/VortexUB)"
    )

    while True:

        await meow()
        file = await event.client.upload_file("vortexautopic.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf vortexautopic.jpg")
        await asyncio.sleep(600)  


CMD_HELP.update(
    {"catsautopic": "➪ `.meowpfp`\nSelects Randomly A Cute Cat Pic And Sets As Your Profile Picture.."}
)
