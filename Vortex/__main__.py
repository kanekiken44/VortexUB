import glob
from Vortex import Vortex
from sys import argv
from telethon import TelegramClient
import Vortex
from Vortex.Config import Var
from Vortex.utils import load_module
from pathlib import Path
import telethon.utils
from Vortex import CMD_HNDLR

PIC = Var.CUSTOM_ALIVE
START_GRP = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT
logo = "VortexUB"

async def add_bot(bot_token):
    await Vortex.start(bot_token)
    Vortex.me = await Vortex.get_me()
    Vortex.uid = telethon.utils.get_peer_id(Vortex.me)


async def startup_log_all_done():
    try:
        await Vortex.send_file(START_GRP, PIC, caption='**Vortex UserBot has been started**')
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

if len(argv) not in (1, 3, 4):
    Vortex.disconnect()
else:
    Vortex.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        Vortex.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        Vortex.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        Vortex.start()

path = 'Vortex/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Vortex Userbot has been deployed! ")

Vortex.loop.run_until_complete(startup_log_all_done())

if len(argv) in {1, 3, 4}:
    Vortex.run_until_disconnected()

else:
    Vortex.disconnect()
