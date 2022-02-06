from telethon import events
import asyncio
from collections import deque
from Vortex.utils import admin_cmd
from Vortex import CMD_HELP

@Vortex.on(admin_cmd(pattern="clock"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"))
	for _ in range(60):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

CMD_HELP.update(
    {
        "clock": "➨ `.clock` \nUse - Clock Clock Clock"
    }
)
