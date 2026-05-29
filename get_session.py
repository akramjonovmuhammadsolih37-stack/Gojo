#!/usr/bin/env python3
"""
Session string olish uchun bir martalik skript.
Faqat bir marta ishlatiladi!

Ishlatish:
  python get_session.py

Natija: SESSION_STRING=... chiqadi
Uni nusxalab .env fayliga yoki server sozlamalariga qo'ying.
"""
import os, sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# ─────────────────────────────────────────
#  API_ID va API_HASH ni .env dan o'qish
# ─────────────────────────────────────────

_api_id_raw = os.environ.get("API_ID", "")
_api_hash   = os.environ.get("API_HASH", "")

if not _api_id_raw or not _api_hash:
    print("=" * 50)
    print("  GOJO-USERBOT — Session olish")
    print("=" * 50)
    print()
    print("[ERROR] API_ID yoki API_HASH topilmadi!")
    print()
    print("Iltimos, avval .env faylini yarating:")
    print("  cp .env.example .env")
    print()
    print("Keyin .env ichiga yozing:")
    print("  API_ID=sizning_api_id")
    print("  API_HASH=sizning_api_hash")
    print()
    print("API ma'lumotlarini https://my.telegram.org dan oling.")
    print("=" * 50)
    sys.exit(1)

try:
    API_ID = int(_api_id_raw)
except ValueError:
    print(f"[ERROR] API_ID son bo'lishi kerak, lekin '{_api_id_raw}' berildi")
    sys.exit(1)

API_HASH = _api_hash

# ─────────────────────────────────────────

print("=" * 50)
print("  GOJO-USERBOT — Session olish")
print("=" * 50)
print()

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    session = client.session.save()
    print()
    print("=" * 50)
    print("✓ Session muvaffaqiyatli olindi!")
    print()
    print("Quyidagi qatorni .env fayliga nusxalang:")
    print()
    print(f"SESSION_STRING={session}")
    print()
    print("=" * 50)
