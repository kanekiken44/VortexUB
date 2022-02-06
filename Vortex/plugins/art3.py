
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from Vortex.utils import admin_cmd

P = ("───▄█▌─▄─▄─▐█▄\n"
"───██▌▀▀▄▀▀▐██\n"
"───██▌─▄▄▄─▐██\n"
"───▀██▌▐█▌▐██▀\n"
"▄██████─▀─██████▄\n")
A = ("░░░░░░░▄█▄▄▄█▄\n"
"▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄\n"
"█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█\n"
"░▐▌░░░░▀▀███▀▀░░░░▐▌\n"
"████░▄█████████▄░████\n")
S = ("▄▄▀█▄───▄───────▄\n"
"▀▀▀██──███─────███\n"
"░▄██▀░█████░░░█████░░\n"
"███▀▄███░███░███░███░▄\n"
"▀█████▀░░░▀███▀░░░▀██▀\n")
D = ("╔══╗░░░░╔╦╗░░╔═════╗\n"
"║╚═╬════╬╣╠═╗║░▀░▀░║\n"
"╠═╗║╔╗╔╗║║║╩╣║╚═══╝║\n"
"╚══╩╝╚╝╚╩╩╩═╝╚═════╝\n")
F = ("───────███\n"
"───────███\n"
"▄█████▄█▀▀\n"
"─▀█████\n"
"──▄████▄\n")

@Vortex.on(admin_cmd(pattern=r"devil"))
async def nandydevil(devil):
    await devil.edit(P)
@Vortex.on(admin_cmd(pattern=r"robot"))
async def nandyrobot(robot):
    await robot.edit(A)
@Vortex.on(admin_cmd(pattern=r"boa"))
async def nandyboa(boa):
    await boa.edit(S)
@Vortex.on(admin_cmd(pattern=r"smile"))
async def nandysmile(smile):
    await smile.edit(D)
@Vortex.on(admin_cmd(pattern=r"toilet"))
async def nandytoilet(toilet):
    await toilet.edit(F)
