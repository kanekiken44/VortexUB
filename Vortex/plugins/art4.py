
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from Vortex.utils import admin_cmd

G = ("▄█▀─▄▄▄▄▄▄▄─▀█▄\n"
"▀█████████████▀\n"
"────█▄███▄█\n"
"─────█████\n"
"─────█▀█▀█\n")
H = ("───▄▄─▄████▄▐▄▄▄▌\n"
"──▐──████▀███▄█▄▌\n"
"▐─▌──█▀▌──▐▀▌▀█▀\n"
"─▀───▌─▌──▐─▌\n"
"─────█─█──▐▌█\n")
J = ("──▄──▄────▄▀\n"
"───▀▄─█─▄▀▄▄▄\n"
"▄██▄████▄██▄▀█▄\n"
"─▀▀─█▀█▀▄▀███▀\n"
"──▄▄▀─█──▀▄▄\n")
K = ("░╔╔╩╩╝\n"
"▄██▄\n"
"░░██████▄░░░░░░▄▄▄▄▄▄█\n"
"░░█▀█▀█▀█░░▄░▄████████\n"
"░▄▌▄▌▄▌▄▌░▀▄▄▄▄█▄▄▄▄█▄\n")
L = ("█───▄▀▀▀▀▄─▐█▌▐█▌▐██\n"
"█──▐▄▄────▌─█▌▐█─▐▌─\n"
"█──▐█▀█─▀─▌─█▌▐█─▐██\n"
"█──▐████▄▄▌─▐▌▐▌─▐▌─\n"
"███─▀████▀───██──▐██\n")

@Vortex.on(admin_cmd(pattern=r"bull"))
async def nandybull(bull):
    await bull.edit(G)
@Vortex.on(admin_cmd(pattern=r"fox"))
async def nandyfox(fox):
    await fox.edit(H)
@Vortex.on(admin_cmd(pattern=r"spider"))
async def nandyspider(spider):
    await spider.edit(J)
@Vortex.on(admin_cmd(pattern=r"winter"))
async def nandywinter(winter):
    await winter.edit(K)
@Vortex.on(admin_cmd(pattern=r"love"))
async def nandylove(love):
    await love.edit(L)
