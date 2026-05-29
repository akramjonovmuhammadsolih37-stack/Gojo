import asyncio
from telethon import TelegramClient, events
import zeus.client
from time import sleep
client = zeus.client.client


PLUGIN_NAME = "snow"
PLUGIN_DESC = "Qor animatsiyasi"
COMMANDS = {'.snow': "Qor yog'ish animatsiyasi"}

@events.register(events.NewMessage(pattern=".snow", outgoing=True))
async def snow(message):
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit(' ☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n   ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')  
	await asyncio.sleep(1.25) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️  \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
	await asyncio.sleep(0.75) 
	await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')