import streamlit as st
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Çevre değişkenlerini yükle
load_dotenv()

# Sayfa yapılandırması
st.set_page_config(
    page_title="Jarvis AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Özel CSS - Uzay Siyahı Tema
st.markdown("""
<style>
    body {
        background-color: #1a1a1a;
        color: #e0e0e0;
    }
    .stApp {
        background-color: #1a1a1a;
    }
    .stTextInput > div > div > input {
        background-color: #2b2b2b;
        color: #e0e0e0;
    }
    .stButton > button {
        background-color: #0096FF;
        color: white;
    }
    h1 {
        color: #0096FF;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# OpenRouter API Yapılandırması
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = "openrouter/auto"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

# Session State Başlatma
if "messages" not in st.session_state:
    st.session_state.messages = []

if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "Senin adın Jarvis. Bir AI asistanısın. Kibar, yardımcı ve zekisin. Türkçe konuş."

if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = bool(OPENROUTER_API_KEY)

# Başlık
st.markdown("<h1>🤖 Jarvis AI Asistanı</h1>", unsafe_allow_html=True)

# Sidebar - Ayarlar
with st.sidebar:
    st.markdown("### ⚙️ Ayarlar")
    
    # API Anahtarı
    if not st.session_state.api_key_set:
        api_key_input = st.text_input(
            "OpenRouter API Anahtarı",
            type="password",
            placeholder="sk-or-..."
        )
        if api_key_input:
            st.session_state.api_key_set = True
            OPENROUTER_API_KEY = api_key_input
            st.success("✅ API Anahtarı kaydedildi!")
    else:
        st.success("✅ API Anahtarı yapılandırıldı")
    
    # Sistem Promptu
    st.markdown("### 📝 Sistem Promptu")
    new_prompt = st.text_area(
        "Jarvis'in davranışını özelleştir:",
        value=st.session_state.system_prompt,
        height=100
    )
    if new_prompt != st.session_state.system_prompt:
        st.session_state.system_prompt = new_prompt
        st.session_state.messages = []
        st.success("✅ Sistem promptu güncellendi!")
    
    # Sohbet Geçmişini Temizle
    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.messages = []
        st.success("✅ Sohbet geçmişi temizlendi!")

# OpenRouter API ile iletişim
def get_ai_response(user_message):
    if not OPENROUTER_API_KEY:
        return "❌ Hata: OpenRouter API anahtarı yapılandırılmadı. Lütfen sidebar'dan API anahtarınızı girin."
    
    # Sistem promptu ve mesaj geçmişini hazırla
    messages = [{"role": "system", "content": st.session_state.system_prompt}]
    
    # Önceki mesajları ekle
    for msg in st.session_state.messages:
        messages.append(msg)
    
    # Yeni kullanıcı mesajını ekle
    messages.append({"role": "user", "content": user_message})
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": messages
    }
    
    try:
        response = requests.post(OPENROUTER_BASE_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"]
        else:
            return "❌ Hata: API'den geçerli bir yanıt alınamadı."
    except requests.exceptions.RequestException as e:
        return f"❌ Hata: {str(e)}"

# Sistem Kontrolleri
def get_system_info(command):
    if "saat" in command.lower():
        return f"Şu anki saat: {datetime.now().strftime('%H:%M:%S')}"
    elif "tarih" in command.lower():
        return f"Bugünün tarihi: {datetime.now().strftime('%d.%m.%Y')}"
    elif "sistem" in command.lower():
        return "Sistem bilgisi: Python tabanlı Streamlit web uygulaması"
    return None

# Chat Arayüzü
st.markdown("### 💬 Sohbet")

# Mesaj Geçmişini Göster
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'**👤 Siz:** {message["content"]}')
        else:
            st.markdown(f'**🤖 Jarvis:** {message["content"]}')

# Mesaj Giriş Alanı
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Mesajınızı yazın...",
        placeholder="Merhaba Jarvis!",
        key="user_input"
    )

with col2:
    send_button = st.button("📤 Gönder", use_container_width=True)

# Mesaj İşleme
if send_button and user_input:
    # Sistem komutlarını kontrol et
    system_response = get_system_info(user_input)
    
    if system_response:
        response = system_response
    else:
        # AI'dan yanıt al
        response = get_ai_response(user_input)
    
    # Mesajları session state'e ekle
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sayfayı yenile
    st.rerun()

# Footer
st.markdown("""
---
<div style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 2rem;">
    <p>🤖 Jarvis AI Asistanı | OpenRouter API Powered</p>
</div>
""", unsafe_allow_html=True)
