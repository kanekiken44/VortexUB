from telethon.tl.types import Channel

from Vortex import *
from Vortex import ALIVE_NAME, bot, Vortexversion
from Vortex.Config import Config, Var

if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

VORTEXUSER = str(ALIVE_NAME) if ALIVE_NAME else "Vortex Userbot Is Up And Running...."

vortex = f"Vortex version: {Vortexversion}\n"
vortex += f"Log group: {log}\n"
vortex += f"Assistant: {bots}\n"
vortex += f"Sudo: {sudo}\n"
vortex += f"PMSecurity: {pm}\n"
vortex += f"\nVisit @VortexUBSupport for any help.\n"
vortexstats = f"{Vortex}"

THEFIRST_NAME = bot.me.first_name
OWNER_ID = bot.me.id


async def vortex_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a

Crew = [1517994352, 2125081807, 2087717046, 5068636535]

resgrp = [-1001321613309, -1001338988490]
