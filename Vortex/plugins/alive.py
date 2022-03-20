
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Vortex import ALIVE_NAME, CMD_HELP, Vortexversion
from Vortex.__init__ import StartTime
from Vortex.Config import Config, Var

START_PIC = "https://telegra.ph/file/cc29c25774e5906547310.jpg"

CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Vortex is Alive"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else START_PIC
alivemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "🖤️"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@VortexUB"


@Vortex.on(admin_cmd(outgoing=True, pattern="alive"))
@Vortex.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def ifiamalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    vortex = f"**The Vortex Userbot is Running.....**\n\n"
    vortex += f"`{CUSTOM_ALIVE}`\n\n"
    vortex += f"┏━━━━━━━━━━━━━━━━━━━\n"
    vortex += (
        f"┣➣ **Telethon Version**: `1.17`\n┣➣ **Python**: `3.9.2`\n"
    )
    vortex += f"┣➣ **Vortex Version**: `{Vortexversion}`\n"
    vortex += f"┣➣ **Support**: @VortexUBSupport\n"
    vortex += f"┣➣ **Sudo** : `{sudo}`\n"
    vortex += f"┣➣ **Uptime**: `{uptime}`\n"
    vortex += (
        f"┣➣ {alivemoji} **My Master** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
    )
    vortex += f"┗━━━━━━━━━━━━━━━━━━━\n"
    vortex += "    [Repo](https://github.com/Kanekiken44/Vortex-deploy)"
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, ALV_PIC, caption=vortex, link_preview=False)
    await alive.delete()
        


CMD_HELP.update({"alive": "➨ `.alive`\nUse - Check is it Alive or Dead(RIP)."})
