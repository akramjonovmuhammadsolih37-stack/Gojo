#!/usr/bin/env python3
"""
GOJO-USERBOT — Asosiy fayl
Yangi plugin qo'shish uchun: zeus/ papkasiga .py fayl qo'ying!
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

# Render'da bot o'chib qolmasligi uchun keep-alive
try:
    from keep_alive import keep_alive
    keep_alive()
    print("[OK] Keep-alive server ishga tushdi!")
except Exception as e:
    print(f"[INFO] Keep-alive yo'q: {e}")

# ─────────────────────────────────────────
import zeus.client
client = zeus.client.client

# ─────────────────────────────────────────
# AVTOMATIK PLUGIN LOADER
# ─────────────────────────────────────────

SKIP_FILES = {"client.py", "__init__.py"}

plugin_files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "zeus", "*.py")))

loaded = []
failed = []

for filepath in plugin_files:
    filename = os.path.basename(filepath)
    if filename in SKIP_FILES:
        continue

    module_name = f"zeus.{filename[:-3]}"
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "HANDLERS"):
            for handler in module.HANDLERS:
                client.add_event_handler(handler)
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
