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
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background-color: #1a1a1a;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background-color: #1a1a1a;
        padding: 0;
    }
    
    .stApp {
        background-color: #1a1a1a;
    }
    
    /* Chat mesajları */
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        font-size: 0.95rem;
    }
    
    .user-message {
        background-color: #0096FF;
        color: white;
        margin-left: 2rem;
        text-align: right;
    }
    
    .ai-message {
        background-color: #2b2b2b;
        color: #e0e0e0;
        margin-right: 2rem;
        border-left: 3px solid #0096FF;
    }
    
    /* Giriş alanı */
    .stTextInput > div > div > input {
        background-color: #2b2b2b;
        color: #e0e0e0;
        border: 1px solid #444;
        border-radius: 0.5rem;
    }
    
    .stButton > button {
        background-color: #0096FF;
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #0077CC;
        transform: translateY(-2px);
    }
    
    /* Başlık */
    h1 {
        color: #0096FF;
        text-align: center;
        margin-bottom: 1rem;
        font-size: 2.5rem;
        text-shadow: 0 0 20px rgba(0, 150, 255, 0.3);
    }
    
    /* Parçacık animasyonu konteyner */
    .particle-container {
        width: 100%;
        height: 300px;
        background: linear-gradient(135deg, #1a1a1a 0%, #2b2b2b 100%);
        border-radius: 1rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        border: 1px solid #0096FF;
        box-shadow: 0 0 30px rgba(0, 150, 255, 0.1);
    }
    
    /* Ayarlar paneli */
    .settings-panel {
        background-color: #2b2b2b;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 3px solid #0096FF;
        margin-bottom: 1rem;
    }
    
    .settings-panel label {
        color: #0096FF;
        font-weight: 600;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .settings-panel input,
    .settings-panel textarea {
        background-color: #1a1a1a;
        color: #e0e0e0;
        border: 1px solid #444;
        border-radius: 0.5rem;
        padding: 0.5rem;
        width: 100%;
        margin-bottom: 1rem;
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
    st.session_state.system_prompt = "Senin adın Jarvis. Bir AI asistanısın. Kibar, yardımcı ve zekisin. Türkçe konuş. Sistem bilgilerine erişebilirsin (saat, tarih vb.)."

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
        st.session_state.messages = []  # Sohbet geçmişini temizle
        st.success("✅ Sistem promptu güncellendi!")
    
    # Sohbet Geçmişini Temizle
    if st.button("🗑️ Sohbeti Temizle"):
        st.session_state.messages = []
        st.success("✅ Sohbet geçmişi temizlendi!")

# Parçacık Animasyonu (HTML/CSS/JS ile)
st.markdown("""
<div class="particle-container" id="particleContainer"></div>

<script>
    const canvas = document.createElement('canvas');
    const container = document.getElementById('particleContainer');
    if (container) {
        container.appendChild(canvas);
        const ctx = canvas.getContext('2d');
        canvas.width = container.offsetWidth;
        canvas.height = container.offsetHeight;
        
        const particles = [];
        const particleCount = 100;
        
        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.vx = (Math.random() - 0.5) * 2;
                this.vy = (Math.random() - 0.5) * 2;
                this.radius = Math.random() * 2 + 1;
                this.baseRadius = this.radius;
            }
            
            update() {
                this.x += this.vx;
                this.y += this.vy;
                
                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
                
                // Merkeze çekim
                const dx = canvas.width / 2 - this.x;
                const dy = canvas.height / 2 - this.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist > 150) {
                    this.vx += dx * 0.0005;
                    this.vy += dy * 0.0005;
                }
            }
            
            draw() {
                ctx.fillStyle = 'rgba(0, 150, 255, 0.7)';
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fill();
            }
        }
        
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }
        
        function animate() {
            ctx.fillStyle = 'rgba(26, 26, 26, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            
            // Yakın parçacıklar arası çizgiler
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 50) {
                        ctx.strokeStyle = `rgba(0, 150, 255, ${0.2 * (1 - dist / 50)})`;
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
            
            requestAnimationFrame(animate);
        }
        
        animate();
    }
</script>
""", unsafe_allow_html=True)

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
            st.markdown(f'<div class="chat-message user-message">👤 {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message ai-message">🤖 {message["content"]}</div>', unsafe_allow_html=True)

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
    <p>Mobil uyumlu • Uzay Siyahı Tema • Açık Kaynak</p>
</div>
""", unsafe_allow_html=True)
