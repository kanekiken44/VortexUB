import asyncio
from telethon import events
from Vortex.utils import admin_cmd
from Vortex import CMD_HELP

@Vortex.on(admin_cmd("support"))
async def support(event):
    if event.fwd_from:
        return
    await event.edit(
        "🖤**Vortex UserBot**🖤\n"
        "𒊹︎︎︎[Vortex](https://t.me/VortexUB)\n"
        "𒊹︎︎︎[Support Group](https://t.me/VortexUBsupport)\n"
        "𒊹︎︎︎[GitHub Profile](https://github.com/kanekiken44)\n"
)

@Vortex.on(admin_cmd("docs"))
async def docs(event):
    await event.edit(
        "🖤**Vortex UserBot**🖤\n"
        "~[Vortex](https://t.me/VortexUB)\n"
        "~[Repo](https://github.com/kanekiken44/VortexUB)\n"
)

CMD_HELP.update(
    {
        "misc": " `.support` \
\nUse - : Support.\
\n\n `.docs` \
\nUse - : Docs."
    }
)
