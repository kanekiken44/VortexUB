
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from Vortex.utils import admin_cmd

T = ("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
Y = ("──────▄▀─\n"
"─█▀▀▀█▀█─\n"
"──▀▄░▄▀──\n"
"────█────\n"
"──▄▄█▄▄──\n")
U = ("─▄▀▀███═◯\n"
"▐▌▄▀▀█▀▀▄\n"
"█▐▌─────▐▌\n"
"█▐█▄───▄█▌\n"
"▀─▀██▄██▀\n")
I = ("───────────▀▄\n"
"──█▄▄▄▄▄███▀▄─▄▄\n"
"▄▀──▀▄─▀▀█▀▀▄▀──▀▄\n"
"▀▄▀▀█▀▀████─▀▄──▄▀\n"
"──▀▀──────────▀▀\n")
O = ("O────────────────O\n"
"█▓██▄────────────█\n"
"█▓▓░▀▄▀░░░░░░░░░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█────────────────█\n")

@Vortex.on(admin_cmd(pattern=r"welcome"))
async def nandywelcome(welcome):
    await welcome.edit(T)
@Vortex.on(admin_cmd(pattern=r"drink"))
async def nandydrink(drink):
    await drink.edit(Y)
@Vortex.on(admin_cmd(pattern=r"bomb"))
async def nandybomb(bomb):
    await bomb.edit(U)
@Vortex.on(admin_cmd(pattern=r"bike"))
async def nandybike(bike):
    await bike.edit(I)
@Vortex.on(admin_cmd(pattern=r"goodnight"))
async def nandygoodnight(goodnight):
    await goodnight.edit(O)
