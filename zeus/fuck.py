from telethon import TelegramClient, events
import zeus.client
client = zeus.client.client


PLUGIN_NAME = "fuck"
PLUGIN_DESC = "Haqorat animatsiyasi"
COMMANDS = {'.fuck': 'Haqorat animatsiyasi'}

@events.register(events.NewMessage(pattern=".fuck"))
async def fuck(event):
	await event.edit("┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┗━┻━┻━┻┛┗━━━┛")