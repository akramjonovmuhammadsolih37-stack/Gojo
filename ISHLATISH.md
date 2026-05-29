# 🚀 GOJO-USERBOT — Ishga tushirish

## Lokal (o'z kompyuterda)

```bash
# 1. Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 2. .env fayl yaratish
cp .env.example .env

# 3. Session olish
python get_session.py
# Chiqgan SESSION_STRING ni .env ga yozing

# 4. Serverni ishga tushirish
python server.py

# 5. Brauzerda oching
# http://localhost:5000
```

**Login:** admin / (terminal da chiqgan parol)

---

## Hosting (Railway / Render / VPS)

### Railway / Render
```
Start command: python server.py
Environment variables:
  ADMIN_PASSWORD = (o'zingizning parolingiz)
  SESSION_STRING = (get_session.py dan)
```

### VPS (Ubuntu)
```bash
pip install -r requirements.txt
cp .env.example .env
nano .env  # to'ldiring

# Fon rejimida ishlatish
nohup python server.py > server.log 2>&1 &

# Yoki screen bilan
screen -S gojo
python server.py
# Ctrl+A, D — chiqish
```

---

## Admin panel

1. `http://server_ip:5000` ga kiring
2. Login: `admin` + terminelda chiqgan parol
3. Admin panel → yuqori chap menyu

## Yangi foydalanuvchi

Ro'yxatdan o'tish tab → username + parol (min 6 belgi)

