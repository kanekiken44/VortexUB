from telethon import functions

from Vortex import CMD_HELP
from Vortex.utils import admin_cmd


@Vortex.on(admin_cmd(pattern=r"listmyusernames", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


CMD_HELP.update(
    {
          "listmyreserved_usernames": ".listmyusernames\nUse - Shows all usernames you have reserved."
    }
)
