from geopy.geocoders import Nominatim
from telethon.tl import types

from Vortex import CMD_HELP
from Vortex.utils import admin_cmd


@Vortex.on(admin_cmd(pattern="gps ?(.*)"))
@Vortex.on(sudo_cmd(pattern="gps ?(.*)", allow_sudo=True))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await eor(event, "Please give me a location to find.")

    await eor(event, "Finding...")

    geolocator = Nominatim(user_agent="Rizoeluserbot")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await eor(event, "Sorry, no results found")


CMD_HELP.update({"gps": ".gps <location>\nUse - Gps location on map."})
