import asyncio
import requests
import urllib
import json
import os
from telethon import events
from Vortex.utils import admin_cmd
from Vortex import CMD_HELP

@Vortex.on(admin_cmd(pattern="animepic"))
async def _(event):
    if event.fwd_from:
        return
    with urllib.request.urlopen(
            "https://api.waifu.pics/sfw/waifu"
    ) as url:
        data = json.loads(url.read().decode())
    finalcat = (data['url'])
    r = requests.get(finalcat, allow_redirects=True)
    open('animepicvortex.jpg', 'wb').write(r.content)
    await Vortex.send_file(
                        event.chat_id,
                        'animepicvortex.jpg',
                        caption=f"Here's Your Waifu..\nGathered By Your Vortex userbot",
                    )
    os.system("rm animepicvortex.jpg")

CMD_HELP.update(
    {
        "animepics": "➨ `.animepic \nUse - Get Random Waifu Images"
    }
)
