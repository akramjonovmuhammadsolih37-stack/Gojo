from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys

# ═══════════════════════════════════════════
#  GOJO-USERBOT — Client sozlamalari
#  Barcha qiymatlar .env faylidan o'qiladi
# ═══════════════════════════════════════════

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ─────────────────────────────────────────
#  Majburiy o'zgaruvchilarni tekshirish
# ─────────────────────────────────────────

_missing = []

_api_id_raw = os.environ.get("API_ID", "")
if not _api_id_raw:
    _missing.append("API_ID")

_api_hash = os.environ.get("API_HASH", "")
if not _api_hash:
    _missing.append("API_HASH")

SESSION = os.environ.get("SESSION_STRING", "")
if not SESSION:
    _missing.append("SESSION_STRING")

if _missing:
    print("[ERROR] Quyidagi o'zgaruvchilar .env faylida topilmadi:")
    for m in _missing:
        print(f"  ✗  {m}")
    print()
    print("[INFO]  .env.example faylini nusxalab .env qiling:")
    print("[INFO]    cp .env.example .env")
    print("[INFO]  Keyin SESSION_STRING olish uchun:")
    print("[INFO]    python get_session.py")
    sys.exit(1)

try:
    API_ID = int(_api_id_raw)
except ValueError:
    print(f"[ERROR] API_ID son bo'lishi kerak, lekin '{_api_id_raw}' berildi")
    sys.exit(1)

API_HASH = _api_hash

# Bot token — help.py uchun (ixtiyoriy)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# ═══════════════════════════════════════════

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# botClient — help.py inline query uchun kerak (ixtiyoriy)
botClient = None
if BOT_TOKEN:
    botClient = TelegramClient("bot_session", API_ID, API_HASH)
    botClient.start(bot_token=BOT_TOKEN)
