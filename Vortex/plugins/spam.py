import asyncio
import os
from asyncio import sleep

from telegraph import Telegraph, upload_file
from Vortex.plugins import resgrp
from Vortex.Config import Config

from .. import CMD_HELP

LOGGER_GROUP = Var.PRIVATE_GROUP_ID
LOGGER = True
path = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.isdir(path):
    os.makedirs(path)
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]



@Vortex.on(admin_cmd(pattern="tspam"))
@Vortex.on(sudo_cmd(pattern="tspam", allow_sudo=True))
async def tmeme(e):
    tspam = str(e.text[7:])
    if int(e.chat_id) in resgrp:
                text = f"Sorry !! I can't spam here"
                await e.respond(text, parse_mode=None, link_preview=None )
    else:
        message = tspam.replace(" ", "")
        for letter in message:
            await e.respond(letter)
        await e.delete()


@Vortex.on(admin_cmd(pattern="spam"))
@Vortex.on(sudo_cmd(pattern="spam", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        if int(e.chat_id) in resgrp:
                text = f"Sorry !! I can't spam here"
                await e.respond(text, parse_mode=None, link_preview=None )
        else:
            counter = int(message[6:8])
            spam_message = str(e.text[8:])
            await asyncio.wait([e.respond(spam_message) for i in range(counter)])
            await e.delete()
            if LOGGER:
                await e.client.send_message(
                    LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@Vortex.on(admin_cmd(pattern="bigspam"))
@Vortex.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        if int(e.chat_id) in resgrp:
                text = f"Sorry !! I can't spam here"
                await e.respond(text, parse_mode=None, link_preview=None )
        else:
            counter = int(message[9:13])
            spam_message = str(e.text[13:])
            for i in range(1, counter):
                await e.respond(spam_message)
            await e.delete()
            if LOGGER:
                await e.client.send_message(
                    LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )



@Vortex.on(admin_cmd(pattern="delayspam (.*)"))
@Vortex.on(sudo_cmd(pattern="delayspam (.*), allow_sudo=True"))
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(" ", 2)[0])
    if int(e.chat_id) in resgrp:
                text = f"Sorry !! I can't spam here"
                await e.respond(text, parse_mode=None, link_preview=None )
    else:
        counter = int(e.pattern_match.group(1).split(" ", 2)[1])
        spam_message = str(e.pattern_match.group(1).split(" ", 2)[2])
        await e.delete()
        for i in range(1, counter):
            await e.respond(spam_message)
            await sleep(spamDelay)
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#DelaySPAM\n" "DelaySpam was executed successfully"
        )


CMD_HELP.update(
    {
        "spam": ".tspam <sentence>\nUse - Spams text\
        \n\n.spam <number> <sentence>\nUse - Spams\
        \n\n.bigspam <number> <sentence>\nUse - A Big Spam\
        \n\n.delayspam <time> <word>\nUse - Spam, with some setted delay!"
    }
)
