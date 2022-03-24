import time
from datetime import datetime

from Vortex import CMD_HELP
from Vortex.__init__ import StartTime


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


# @command(pattern="^.ping$")


@Vortex.on(admin_cmd(pattern="ping$"))
@Vortex.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("🗼Pong!🗼")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    await event.edit(
        f" **┏━━━┳━━┳━┓╋┏┳━━━┓\n┃┏━┓┣┫┣┫┃┗┓┃┃┏━┓┃\n┃┗━┛┃┃┃┃┏┓┗┛┃┃╋┗┛\n┃┏━━┛┃┃┃┃┗┓┃┃┃┏━┓\n┃┃╋╋┏┫┣┫┃╋┃┃┃┗┻━┃\n┗┛╋╋┗━━┻┛╋┗━┻━━━┛**\n ᴘᴏɴɢ sᴘᴇᴇᴅ : `{ms}`\n🖤️ **VortexUserbot Uptime** : `{uptime}`".format(
            ms)
    )


CMD_HELP.update(
    {"ping": ".ping\nUse - See the ping stats and uptime of userbot."})

