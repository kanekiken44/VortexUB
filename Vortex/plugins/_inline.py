#copy Right by Karlex lol

import asyncio
import html
import os
import re
from math import ceil

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest

from Vortex import ALIVE_NAME, CMD_HELP, CMD_LIST, CUSTOM_PMPERMIT, bot, Vortex
from Vortex.plugins import vortexstats
from Vortex.Config import Var

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
VORTEXPIC = PMPERMIT_PIC or "https://telegra.ph/file/54e6ac31560703b490821.jpg"
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
lightningbot = Var.TG_BOT_USER_NAME_BF_HER
botname = lightningbot if lightningbot.startswith("@") else f"@{lightningbot}"
LOG_GP = Var.PRIVATE_GROUP_ID
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`Heyo! I am Vortex userbot! Please wait for my master to approve you, Don't ever try to spam"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Vortex Is Alive"
USER_BOT_WARN_ZERO = "`I told you Don't spam. Now you have been automatically blocked and reported until further notice.`\n\n**GoodBye Dumbass!** "

if Var.LOAD_MYBOT == "False":
    USER_BOT_NO_WARN = (
        "**I am Vortex userbot And My Master Is [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\nPlease choose why you are here, from the available options\n".format(
            DEFAULTUSER, myid, MESAG
        )
    )

elif Var.LOAD_MYBOT == "True":
    USER_BOT_NO_WARN = (
        "**I am Vortex userbot And My Master Is [{}](tg://user?id={})**\n\n"
        "{}\n\n"
        "For Emergency Or if you are banned, PM me via {}"
        "\nSelect any one reason for disturbing my master, from the available options\n\n".format(
            DEFAULTUSER, myid, MESAG, botname
        )
    )
CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "🖤")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 3))

if Var.TG_BOT_USER_NAME_BF_HER is not None and Vortex is not None:

    @bot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("`Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "Vortexuserbot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Vortexuserbot Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n__Bot is functioning normally, master!__\n\n(c) @VortexUBsupport",
                buttons=[
                    [custom.Button.inline("Stats", data="statcheck")],
                    [Button.url("Repo", "https://GitHub.com/Kanekiken44/Vortex-deploy")],
                    [
                        Button.url(
                            "Deploy Your Own!",
                            "https://t.me/VortexUBSupport",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query.startswith("**PM"):
            VORTEXBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=VORTEXPIC,
                text=VORTEXBT,
                buttons=[
                    [
                        custom.Button.inline("Request", data="req"),
                        custom.Button.inline("Chat", data="chat"),
                    ],
                    [custom.Button.inline("To Spam ❌", data="heheboi")],
                    [custom.Button.inline("What Is This ❓", data="pmclick")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text="Vortexuserbot - Telegram Userbot by Team Vortex",
                buttons=[
                    [
                        Button.url(
                            "Repo", "https://GitHub.com/Kanekiken44/Vortex-deploy"
                        ),
                        Button.url(
                            "Deploy Your Own",
                            "https://t.me/VortexUBSupport",
                        ),
                    ],
                    [Button.url("Vortexuserbot", "https://t.me/VortexUBSupport")],
                ],
            )

        else:
            result = builder.article(
                "Source Code",
                text="**Welcome to Vortexuserbot**\n\n`Click below buttons for more`",
                buttons=[
                    [custom.Button.url("✨SUPPORT✨", "https://t.me/VortexUBSupport")],
                    [
                        custom.Button.url(
                            "GITHUB", "https://GitHub.com/Kanekiken44/Vortex-deploy"
                        ),
                        custom.Button.url(
                            "Deploy Your Own",
                            "https://t.me/VortexUBSupport",
                        ),
                    ],
                    [
                        custom.Button.url(
                            "Team Vortex", "https://t.me/TeamVortexUB"
                        )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @bot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
           
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Please make your own Vortexuserbot by @VortexUB , and don't use mine!"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, Master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"I am Vortexuserbot!! Here {DEFAULTUSER} to protect my master from unknown inboxing persons.\n\nI am [Vortexuserbot](t.me/VortexUB)"
            )

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reopen")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit("Menu Re-opened", buttons=buttons)
        else:
            reply_pop_up_alert = "This bot ain't for u!!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Okay, `{DEFAULTUSER}` will get back to you soon!\nUntil please **wait patiently and don't try to spam! .**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) is **requesting** something in PM!"
            await Vortex.send_message(LOG_GP, tosend)

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ok, So you want to chat...\nPlease wait until  {DEFAULTUSER} approves you or replies, he will be replying soon!\nBut, **don't try spam.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **Random Chatting**!"
            await Vortex.send_message(LOG_GP, tosend)

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"plshelpme")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This ain't for you, master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oh!\n{DEFAULTUSER} My master don't have time to help others...\nBut still send your message **in a single line** and wait till my master respond "
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **help**!"
            await Vortex.send_message(LOG_GP, tosend)

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"heheboi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for unknown inboxers, not for you master!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                "Oh, so you are here to spam \\nDumbass.\\nYou have been automatically blocked until my master unblocks you."
            )

            await borg(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await Vortex.send_message(
                LOG_GP,
                f"[{first_name}](tg://user?id={ok}) tried to **spam** your inbox.\nSo, **blocked him**",
            )

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
                "Menu Closed!!", buttons=[Button.inline("Re-open Menu", data="reopen")]
            )
        else:
            reply_pop_up_alert = "Please deploy own userbot from @VortexUBSupport"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statcheck")))
    async def rip(event):
        text = vortexstats
        await event.answer(text, alert=True)

    @bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Please get your own Userbot, and don't use mine!",
                cache_time=0,
                alert=True,
            )
        page = str(event.data_match.group(1).decode("UTF-8"))
        veriler = paginate_help(page, CMD_HELP)
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("`Userbot"):
            rev_text = query[::-1]
            await event.edit(
                "{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=veriler[1],
                link_preview=False,
            )

    @bot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            result = None
            query = event.text
            if event.query.user_id == bot.uid and query.startswith("`Userbot"):
                rev_text = query[::-1]
                await event.edit(text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)), buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @bot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            help_string += f"Commands Available in {plugin_name} - \n"
            try:
                if plugin_name in CMD_HELP:
                    for i in CMD_HELP[plugin_name]:
                        help_string += i
                    help_string += "\n"
                else:
                    for i in CMD_LIST[plugin_name]:
                        help_string += i
                        help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} has no detailed info.\nUse .help {}".format(
                    plugin_name, plugin_name
                )
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                 userbot".format(
                plugin_name
            )
            if len(help_string) >= 14000:
                oops = "Commands are too long!\nSent your saved messages!"
                await event.answer(oops, cache_time=0, alert=True)
                help_string += "\n\nThis will be automatically deleted in 1 minute!"
                if bot is not None and event.query.user_id == bot.uid:
                    ok = await bot.send_message("me", help_string)
                    await asyncio.sleep(60)
                    await ok.delete()
            else:
                buuttons=[Button.inline("Back", data=f"page({page})")]
                await event.edit(reply_pop_up_alert, buttons=buuttons)
        else:
            reply_pop_up_alert = "Please deploy your own Userbot, Don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = HELP_ROWS
    number_of_cols = HELP_COLOUMNS
    vortex = CUSTOM_HELP_EMOJI
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(vortex, x, vortex), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("Close", data="close"),
                custom.Button.inline(
                    "Next", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
