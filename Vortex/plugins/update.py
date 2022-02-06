  
import os
import sys
from Vortex import CMD_HELP, CMD_HNDLR
from Vortex.utils import admin_cmd


@Vortex.on(admin_cmd(pattern="update"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        f" 🖤🖤**Updating Your Vortex UserBot**🖤🖤 ... \n\nPlease Wait Until It Starts Again✅\nFor More, Get Help From [⚡Here⚡](https://t.me/VortexUBSupport) "
    )
    await Vortex.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

CMD_HELP.update(
    {
        "update": "`.update`\nUse - Updates Your Vortexuserbot."
    }
)
