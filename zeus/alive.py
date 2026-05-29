from telethon import TelegramClient, events
import zeus.client
import asyncio
import os
client = zeus.client.client


PLUGIN_NAME = "alive"
PLUGIN_DESC = "Botning ishlash holatini ko'rsatadi"
COMMANDS = {'.alive': "Bot haqida ma'lumot"}

@events.register(events.NewMessage(outgoing=True, pattern=r'.alive'))
async def alive(noob_py):
    client = noob_py.client
    me = await client.get_me()
    username = me.username or str(me.id)
    darknet7719 = await client.download_profile_photo(me.id)
    await noob_py.message.edit("Hayrli kun...")
    await asyncio.sleep(0.5)
    await noob_py.respond("""🥷 **Foydalanuvchi**: @{}

🥷 **Versia**: 1.0.1.3
├╴╴╴╴╴╴╴╴╴╴
└ 🧟‍♀️ **GOJO Userbot**: @volkmedia


🥷 OʻRNATISH 
├╴╴╴╴╴╴╴╴╴╴
├ 👾 https://t.me/volkmedia
└ 👾 https://t.me/volkmedia""".format(username), file=darknet7719 if darknet7719 else None)
    await noob_py.message.delete()
    if darknet7719 and os.path.exists(darknet7719):
        os.remove(darknet7719)
