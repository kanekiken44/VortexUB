import Vortex
from Vortex.plugins.assistant.sql.users_sql import get_user_id
from telethon import events
from telethon.utils import pack_bot_file_id
from Vortex.plugins import OWNER_ID


@Vortex.on(events.NewMessage(func=lambda e: e.is_private))
async def on_out_mssg(event):
    to_send = await event.get_reply_message()
    if to_send is None:
        return
    to_send.id
    send_msg = event.raw_text
    who = event.sender_id
    user_id, reply_message_id = get_user_id(to_send.id)
    if who == OWNER_ID:
        if send_msg.startswith("/"):
            return
        if event.text is not None and event.media:
            # if sending media
            bot_api_file_id = pack_bot_file_id(event.media)
            await Vortex.send_file(user_id, file=bot_api_file_id, caption=event.text, reply_to=reply_message_id)
        else:
            await Vortex.send_message(user_id, send_msg, reply_to=reply_message_id,)
