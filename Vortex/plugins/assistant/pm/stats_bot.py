import Vortex
from Vortex.plugins.assistant.sql.blacklist_sql import all_bl_users
from Vortex.plugins.assistant.sql.userbase_sql import full_userbase
from telethon import events
from Vortex.plugins import OWNER_ID


@Vortex.on(events.NewMessage(pattern="^/stats", from_users=OWNER_ID))
async def rizoel(event):
    thevortex = len(full_userbase())
    noyoulight = len(all_bl_users())
    await Vortex.send_message(event.chat_id,
                             "Here is the stats for your bot:\nTotal Users = {}\nBlacklisted Users = {}".format(therizoel, noyoulight)
                             )
