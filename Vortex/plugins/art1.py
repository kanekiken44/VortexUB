
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from Vortex import ALIVE_NAME
from Vortex.utils import admin_cmd


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.hacker$")
@Vortex.on(admin_cmd(pattern=r"hacker"))
async def nandyhacker(hacker):
    await hacker.edit(n + "Anonymous \n"
"─────█─▄▀█──█▀▄─█─────\n"
"────▐▌──────────▐▌────\n"
"────█▌▀▄──▄▄──▄▀▐█────\n"
"───▐██──▀▀──▀▀──██▌───\n"
"──▄████▄──▐▌──▄████▄──\n")


Q = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n")
W = ("──────▄▀▄─────▄▀▄\n"
"─────▄█░░▀▀▀▀▀░░█▄\n"
"─▄▄──█░░░░░░░░░░░█──▄▄\n"
"█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n")
E = ("▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒\n"
"▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒\n"
"▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒\n"
"▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒\n"
"▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒\n")
R = ("░▄▄▄▄░\n"
"▀▀▄██►\n"
"▀▀███►\n"
"░▀███►░█►\n"
"▒▄████▀▀\n")

@Vortex.on(admin_cmd(pattern=r"teddy"))
async def nandyteddy(teddy):
    await teddy.edit(Q)
@Vortex.on(admin_cmd(pattern=r"cat"))
async def nandycat(cat):
    await cat.edit(W)
@Vortex.on(admin_cmd(pattern=r"alien"))
async def nandyalien(alien):
    await alien.edit(E)	
@Vortex.on(admin_cmd(pattern=r"dinosaur"))
async def nandydinosaur(dinosaur):
    await dinosaur.edit(R)
