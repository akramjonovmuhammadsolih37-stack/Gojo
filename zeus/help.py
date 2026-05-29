from telethon import TelegramClient, events, functions, types, Button
import zeus.client
client = zeus.client.client
botClient = zeus.client.botClient

# botClient ixtiyoriy — faqat BOT_TOKEN berilsa ishlaydi
if botClient:
    @botClient.on(events.InlineQuery)
    async def _(query):
        if query.text == "ppphelp":
            result = query.builder.article('ppphelp', text="GOJO USERBOT HELP MENU", buttons=[
                [Button.inline("Bombs", data=b"1"), Button.inline("magic", data=b"2"), Button.inline("loading", data=b"3")],
                [Button.inline("Dump", data=b"4"), Button.inline("18+", data=b"5"), Button.inline("LUL", data=b"6")],
                [Button.inline("Snake", data=b"7"), Button.inline("NotHappy", data=b"8"), Button.inline("Muah", data=b"9")],
                [Button.inline("Tmoon", data=b"10"), Button.inline("Smoon", data=b"11"), Button.inline("moon", data=b"12")],
                [Button.inline("Clock", data=b"13"), Button.inline("Candy", data=b"14"), Button.inline("Heart", data=b"15")],
                [Button.inline("Gymnastic", data=b"16"), Button.inline("clown", data=b"17"), Button.inline("Star", data=b"18")],
                [Button.inline("Earth", data=b"19"), Button.inline("Snow", data=b"20"), Button.inline("Rain", data=b"21")],
                [Button.inline("Clol", data=b"22"), Button.inline("Jio", data=b"23"), Button.inline("Police", data=b"24")]
            ])
            await query.answer([result])

    @botClient.on(events.CallbackQuery)
    async def uzgaruvchi(event):
        answers = {
            b'1': "Animatsia bombs\nplugin: .bombs",
            b'2': "Animatsia Heart emojies\nplugin: .magic",
            b'3': "Animatsia loading\nplugin: .loading",
            b'4': "Animatsia dump\nplugin: .dump",
            b'5': "18+ animation\nplugin: .sexy",
            b'6': "Animatsia lul\nplugin: .lul",
            b'7': "Animatsia Snake\nPlugin: .snake",
            b'8': "Animatsia NotHappy\nplugin: .nothappy",
            b'9': "Animatsia Muah\nPlugin: .muah",
            b'10': "Animatsia Tmoon\nPlugin: .tmoon",
            b'11': "Animatsia Smoon\nPlugin: .smoon",
            b'12': "Animatsia moon\nplugin: .moon",
            b'13': "Animatsia Clock\nplugin: .clock",
            b'14': "Animatsia Candy\nplugin: .candy",
            b'15': "Animatsia Heart\nplugin: .heart",
            b'16': "Animatsia Gymnastik\nplugin: .gym",
            b'17': "Animatsia Clown\nplugin: .clown",
            b'18': "Animatsia Star\nplugin: .star",
            b'19': "Animatsia Earth\nPlugin: .earth",
            b'20': "Animatsia Snow\nplugin: .snow",
            b'21': "Animatsia Rain\nplugin: .rain",
            b'22': "Animatsia clol\nplugin: .clol",
            b'23': "Animatsia jio\nplugin: .jio",
            b'24': "Animatsia police\nplugin: .police",
        }
        msg = answers.get(event.data, "Noma'lum buyruq")
        await event.answer(msg, alert=True)

@events.register(events.NewMessage(pattern=".help", outgoing=True))
async def help(event):
    if not botClient:
        await event.edit(
            "ℹ️ **Help menyusi** uchun `.env` fayliga `BOT_TOKEN` qo'shing.\n"
            "BotFather: https://t.me/BotFather"
        )
        return
    try:
        results = await client.inline_query("@volkrobot", "ppphelp")
        await results[0].click(event.chat_id)
        await event.message.delete()
    except Exception as e:
        await event.edit(f"**Xatolik:** `{e}`")
