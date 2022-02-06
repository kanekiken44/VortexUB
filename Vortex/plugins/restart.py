import os
import sys
from Vortex import CMD_HELP, CMD_HNDLR
from Vortex.utils import admin_cmd


@Vortex.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        f"**Restarting Your Vortexuserbot**.. Please Wait Until It Starts Again "
    )
    await Vortex.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

CMD_HELP.update(
    {
        "restart": ".restart\nUse - Restarts the bot."
    }
)
