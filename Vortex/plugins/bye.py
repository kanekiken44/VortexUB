""" Command:
.bye  """

from telethon import events

import asyncio





@Vortex.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 7)

    input_str = event.pattern_match.group(1)

    if input_str == "bye":

        await event.edit(input_str)

        animation_chars = [
        
            "`Bye🙂🙂`",
            "`Bye I'll come later`",
            "`I think no one loves me😅`",
            "`So`",
            "`I have To Go😢`",
            "`Goodbye😭`",    
            "`Goodbye Until I Comes Back`",
            "`Bye from Me and My VortexUB ️ :)`",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])
