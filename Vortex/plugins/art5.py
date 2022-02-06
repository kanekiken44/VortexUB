
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from Vortex.utils import admin_cmd

Z = ("░▄░█░░░▄▀▀▀▀▀▄░░░█░▄░\n"
"▄▄▀▄░░░█─▀─▀─█░░░▄▀▄▄\n"
"░░░░▀▄▒▒▒▒▒▒▒▒▒▄▀░░░░\n"
"░░░░░█────▀────█░░░░░\n"
"░░░░░█────▀────█░░░░░\n")
X = ("░░░░░░░░░░░░░░░░▄▓▄\n"
"░░░░▄█▄░░░░░░░░▄▓▓▓▄\n"
"░░▄█████▄░░░░░▄▓▓▓▓▓▄\n"
"░▀██┼█┼██▀░░░▄▓▓▓▓▓▓▓▄\n"
"▄▄███████▄▄▄▄▄▄▄▄█▄▄▄▄\n")
C = ("░▄▀▀▀▀▄░░▄▄\n"
"█░░░░░░▀▀░░█░░░░░░▄░▄\n"
"█░║░░░░██░████████████ \n"
"█░░░░░░▄▄░░█░░░░░░▀░▀\n"
"░▀▄▄▄▄▀░░▀▀\n")
V = ("░▄▌░░░░░░░░░▄\n"
"████████████▄\n"
"░░░░░░░░▀▐████\n"
"░░░░░░░░░░░▐██▌\n")
B = ("─────▀▄▀─────▄─────▄\n"
"──▄███████▄──▀██▄██▀\n"
"▄█████▀█████▄──▄█\n"
"███████▀████████▀\n"
"─▄▄▄▄▄▄███████▀\n")

@Vortex.on(admin_cmd(pattern=r"snowman"))
async def nandysnowman(snowman):
    await snowman.edit(Z)
@Vortex.on(admin_cmd(pattern=r"home"))
async def nandyhome(home):
    await home.edit(X)
@Vortex.on(admin_cmd(pattern=r"guitar"))
async def nandyguitar(guitar):
    await guitar.edit(C)
@Vortex.on(admin_cmd(pattern=r"pistol"))
async def nandypistol(pistol):
    await pistol.edit(V)
@Vortex.on(admin_cmd(pattern=r"whale"))
async def nandywhale(whale):
    await whale.edit(B)
