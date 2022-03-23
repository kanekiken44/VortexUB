
import os
from typing import io

from Vortex import *
from Vortex import ALIVE_NAME, CMD_HELP, CMD_HNDLR, CMD_LIST
from Vortex.Config import Config
from Vortex.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Vortex Userbot"
CMD_HNDLR = Config.CMD_HNDLR
CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "🥀")

if CMD_HNDLR is None:
    CMD_HNDLR = "."

@Vortex.on(admin_cmd(outgoing=True, pattern="help ?(.*)"))
async def cmd_list(event):
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    input_str = event.pattern_match.group(1)
    if tgbotusername is None or input_str == "text":
        string = ""
        for i in CMD_HELP:
            string += f'{CUSTOM_HELP_EMOJI} {i} {CUSTOM_HELP_EMOJI}' + "\n"
            for iter_list in CMD_HELP[i]:
                string += f"    `{str(iter_list)}`"
                string += "\n"
            string += "\n"
        if len(string) > 4095:
            with io.BytesIO(str.encode(string)) as out_file:
                out_file.name = "cmd.txt"
                await Vortex.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="**COMMANDS**",
                    reply_to=reply_to_id,
                )
                await event.delete()
        else:
            await event.edit(string)
    elif input_str:
        if input_str in CMD_LIST:
            string = "**Commands available in {}** \n\n".format(input_str)
            if input_str in CMD_HELP:
                for i in CMD_HELP[input_str]:
                    string += i
                string += "\n\n**© @VortexUB**"
            else:
                for i in CMD_LIST[input_str]:
                    string += f"    {i}"
                    string += "\n"
                string += "\n**© @VortexUB**"
            await event.edit(string)
        else:
            await event.edit(f'{input_str} is not a valid plugin!')
    else:
        help_string = f"""`Userbot Helper for {DEFAULTUSER} to reveal all the commands of `**Vortex Userbot**\n\n"""
        try:
            results = await Vortex.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await event.edit(
                f"This bot has inline disabled. Please enable it to use `{CMD_HNDLR}help`.\nGet help from [✨Support Group✨](t.me/VortexUBSupport)"
            )
