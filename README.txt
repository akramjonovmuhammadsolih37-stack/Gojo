═══════════════════════════════════════════════
  GOJO-USERBOT + Web Panel
  To'liq o'rnatish qo'llanmasi
═══════════════════════════════════════════════

📁 FAYLLAR TUZILISHI:
  server.py            — Web panel server
  userbot_panel.html   — Brauzer paneli
  main.py              — Bot asosiy fayli
  get_session.py       — Session olish (1 marta)
  requirements.txt     — Kutubxonalar
  .env.example         — Sozlamalar namunasi
  zeus/                — Bot modullari

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 1-QADAM: O'RNATISH

  pip install -r requirements.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️ 2-QADAM: .env FAYL YARATISH

  .env.example faylini nusxalab .env qiling:

    cp .env.example .env

  Keyin .env faylini oching va API ma'lumotlarini yozing:
    API_ID=     ← https://my.telegram.org dan oling
    API_HASH=   ← https://my.telegram.org dan oling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 3-QADAM: SESSION STRING OLISH
   (Faqat bir marta, telefon kerak)

  python get_session.py

  → Telefon raqam kiriting
  → Telegram kodi kiriting
  → SESSION_STRING=AAAA... chiqadi
  → Uni .env fayliga nusxalang:
      SESSION_STRING=AAAA...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 4-QADAM: SERVERNI ISHGA TUSHIRISH

  python server.py

  Keyin brauzerda oching:
    http://YOUR_VPS_IP:5000

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔐 5-QADAM: PANELGA KIRISH

  Admin parol terminalda avtomatik chiqadi (birinchi ishga tushirganda).
  Yoki .env da o'zingiz belgilang:
    ADMIN_PASSWORD=sizning_parolingiz

  ⚠️ Kirgandan keyin Settings da parolni o'zgartiring!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

▶️ BOT ISHLATISH

  1. Panelga kiring
  2. Dashboard → START BOT bosing
  3. Logs bo'limida real-time natijani koring
  4. Telegram da .help yuboring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 ORQA FONDA ISHLATISH (VPS)

  # Ekranni yopganda ham ishlash uchun:
  nohup python server.py > panel.log 2>&1 &

  # Yoki screen bilan:
  screen -S gojo
  python server.py
  Ctrl+A, D  (ajratish)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ XAVFSIZLIK ESLATMALARI

  • API_ID, API_HASH va SESSION_STRING ni hech kimga bermang!
  • Bu ma'lumotlar faqat .env faylida bo'lishi kerak
  • .env faylini git ga commit qilmang (.gitignore ga qo'shing)

═══════════════════════════════════════════════
