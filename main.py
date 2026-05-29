#!/usr/bin/env python3
"""
GOJO-USERBOT — Asosiy fayl
Yangi plugin qo'shish uchun: zeus/ papkasiga .py fayl qo'ying, shu bo'ldi!
"""
import sys, os, importlib, glob

# Panel loglarini real-time ko'rsatish
class PanelLogger:
    def __init__(self, stream):
        self.stream = stream
    def write(self, msg):
        if msg.strip():
            self.stream.write(msg)
            self.stream.flush()
    def flush(self):
        self.stream.flush()

sys.stdout = PanelLogger(sys.__stdout__)
sys.stderr = PanelLogger(sys.__stderr__)

# ─────────────────────────────────────────
import zeus.client
client = zeus.client.client

# ─────────────────────────────────────────
# AVTOMATIK PLUGIN LOADER
# zeus/ papkasidagi barcha .py fayllarni avtomatik yuklaydi
# client.py ni o'tkazib yuboradi (u asosiy client, plugin emas)
# ─────────────────────────────────────────

SKIP_FILES = {"client.py", "__init__.py"}

plugin_files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "zeus", "*.py")))

loaded = []
failed = []

for filepath in plugin_files:
    filename = os.path.basename(filepath)
    if filename in SKIP_FILES:
        continue

    module_name = f"zeus.{filename[:-3]}"  # .py ni olib tashlash
    try:
        module = importlib.import_module(module_name)

        # Handler ro'yxatini tekshirish (agar plugin HANDLERS = [...] belgilasa)
        if hasattr(module, "HANDLERS"):
            for handler in module.HANDLERS:
                client.add_event_handler(handler)
        else:
            # Eski uslub: modul ichidagi barcha @events.register dekoratorlarni
            # importlash orqali avtomatik ro'yxatdan o'tadi
            pass

        loaded.append(filename)
        print(f"[OK] Plugin yuklandi: {filename}")
    except Exception as e:
        failed.append(filename)
        print(f"[XATO] Plugin yuklanmadi: {filename} — {e}")

print(f"\n[INFO] Jami: {len(loaded)} plugin yuklandi, {len(failed)} xato")
if failed:
    print(f"[XATO] Yuklanmagan pluginlar: {', '.join(failed)}")

print("[OK] GOJO-USERBOT ishga tushdi!\n")

client.start()
print("[OK] Telegram ga ulandi. Buyruqlar tayyor.")
client.run_until_disconnected()
