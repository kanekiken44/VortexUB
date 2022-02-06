from telethon.sync import TelegramClient
from telethon.sessions import StringSession


print("VortexUB")
print("Processing...")
print("CLEARING CACHE...")
print("WAITING FOR SERVER TO RESPOND ")
print("SERVER RESPONDED TIME TAKEN 0.0002 (s)")
print("Vortex REPI LAUNCHED/PROCESSED SUCCESSFULL")

API_KEY = "2239456"
API_HASH = "43839c63dcf38c8cd512f102ede7f618"

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("")
            session = client.session.save()
            client.send_message("me",
            f"**Vortex Session :\n\n`{session}`\n\n**Do not share this anywhere!!!")
            print(
                "Succesfully made String Session"
            )
            print("")
    except:
        print("")
        print("PLZZ ENTER VALID PHONE NUMBER !! ")
        print("")
        continue
    break
