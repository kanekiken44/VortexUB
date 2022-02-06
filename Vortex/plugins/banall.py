#credits - ultraX
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from Vortex.utils import admin_cmd
from Vortex import bot, CMD_HELP


@Vortex.on(admin_cmd(pattern=r"banall", outgoing=True))
async def testing(event):
    vortex = await event.get_chat()
    xd = await event.client.get_me()
    admin = vortex.admin_rights
    creator = vortex.creator
    if not admin and not creator:
        await event.edit("You Don't Have Sufficient Rights")
        return
    await event.edit("Doing Nothing 🙃🙂")
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == xd.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(0.4)
    await event.edit("Nothing Happend here🙃🙂")
    

CMD_HELP.update(
    {
        "banall": "`.banall` in group \nUse - to ban all members in group.\
      "
    }
)


