import os
from dotenv import load_dotenv

# Çevre değişkenlerini yükle
load_dotenv()

# OpenRouter API Yapılandırması
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = "openrouter/auto"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

# Uygulama Yapılandırması
APP_TITLE = "Jarvis AI Asistanı"
APP_VERSION = "1.0.0"

# Tema Renkleri (Uzay Siyahı)
PRIMARY_COLOR = "#0096FF"
BACKGROUND_COLOR = "#1a1a1a"
SECONDARY_BG_COLOR = "#2b2b2b"
TEXT_COLOR = "#e0e0e0"

# Varsayılan Sistem Promptu
DEFAULT_SYSTEM_PROMPT = """Senin adın Jarvis. Bir AI asistanısın. Kibar, yardımcı ve zekisin. 
Türkçe konuş. Sistem bilgilerine erişebilirsin (saat, tarih vb.). 
Kullanıcıların sorularına detaylı ve yararlı cevaplar ver."""
