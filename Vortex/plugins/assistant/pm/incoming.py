import Vortex
from Vortex.plugins.assistant.sql.users_sql import add_user_to_db
from Vortex.plugins.assistant.sql.blacklist_sql import check_is_black_list
from telethon import events
from Vortex.plugins import OWNER_ID


@Vortex.on(events.NewMessage(func=lambda e: e.is_private))
async def one_new_msg(event):
    incoming = event.raw_text
    who = event.sender_id
    if check_is_black_list(who):
        return
    if incoming.startswith("/"):
        pass
    elif who == OWNER_ID:
        return
    else:
        await event.get_sender()
        axel = event.chat_id
        to = await event.forward_to(OWNER_ID)
        add_user_to_db(to.id, who, event.id)
