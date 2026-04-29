# Jarvis Streamlit - Adım Adım Kurulum Rehberi

Bu rehber, Jarvis'i bilgisayarınızda veya telefonunuzda çalıştırmak için gereken tüm adımları içerir.

## 📱 iPhone'da Kurulum (En Kolay Yol)

### Adım 1: Streamlit Cloud'a Yayınla

1. **GitHub Hesabı Oluştur** (yoksa)
   - https://github.com adresine gidin
   - "Sign up" butonuna tıklayın
   - E-mail, şifre ve kullanıcı adı girin

2. **Proje Dosyalarını GitHub'a Yükle**
   - GitHub'da yeni bir repository oluşturun (adı: `jarvis-streamlit`)
   - Proje dosyalarını bu repository'ye yükleyin

3. **Streamlit Cloud'da Yayınla**
   - https://streamlit.io/cloud adresine gidin
   - GitHub hesabınızla giriş yapın
   - "New app" butonuna tıklayın
   - Repository'nizi seçin
   - Branch: `main` (veya `master`)
   - Main file path: `app.py`
   - "Deploy" butonuna basın

4. **Uygulamayı iPhone'a Ekle**
   - Safari'de Streamlit Cloud linkini açın
   - Alttaki **Paylaş** simgesine (yukarı ok) dokunun
   - **Ana Ekrana Ekle** seçeneğini seçin
   - Uygulama adını girin (örn: "Jarvis")
   - **Ekle** butonuna basın

✅ Artık ana ekranınızda Jarvis ikonu olacak!

---

## 💻 Masaüstünde Kurulum

### Windows

**Adım 1: Python Yükle**
1. https://www.python.org/downloads/ adresine gidin
2. "Download Python 3.11" butonuna tıklayın
3. İndirilen dosyayı çalıştırın
4. **"Add Python to PATH" seçeneğini işaretleyin** (çok önemli!)
5. "Install Now" butonuna tıklayın

**Adım 2: Proje Dosyalarını İndir**
1. Proje dosyalarını bilgisayarınıza indirin
2. Klasörü açın (örn: `C:\Users\YourName\jarvis_streamlit_app`)

**Adım 3: Bağımlılıkları Yükle**
1. Windows Başlat menüsünden "Command Prompt" (Komut İstemi) açın
2. Aşağıdaki komutları yazın:
   ```bash
   cd C:\Users\YourName\jarvis_streamlit_app
   pip install -r requirements.txt
   ```

**Adım 4: API Anahtarını Yapılandır**
1. Proje klasöründe `.env` adlı bir dosya oluşturun
2. Aşağıdaki satırı ekleyin:
   ```
   OPENROUTER_API_KEY=sk-or-your-api-key-here
   ```
3. `sk-or-your-api-key-here` kısmını OpenRouter API anahtarınızla değiştirin

**Adım 5: Uygulamayı Çalıştır**
1. Command Prompt'ta aşağıdaki komutu yazın:
   ```bash
   streamlit run app.py
   ```
2. Tarayıcı otomatik olarak açılacak

---

### macOS

**Adım 1: Python Yükle**
1. Terminal'i açın (Spotlight'ta "Terminal" yazın)
2. Aşağıdaki komutu yazın:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Kurulum tamamlandıktan sonra:
   ```bash
   brew install python@3.11
   ```

**Adım 2-5: Windows ile aynı**
(Komut Prompt yerine Terminal kullanın)

---

### Linux (Ubuntu/Debian)

**Adım 1: Python Yükle**
```bash
sudo apt-get update
sudo apt-get install python3.11 python3-pip
```

**Adım 2-5: Windows ile aynı**
(Komut Prompt yerine Terminal kullanın)

---

## 🔑 OpenRouter API Anahtarı Alma

1. https://openrouter.ai adresine gidin
2. Sağ üstte "Sign Up" butonuna tıklayın
3. E-mail ile kayıt olun
4. Dashboard'a gidin
5. Sol tarafta "Keys" seçeneğini tıklayın
6. "Create New Key" butonuna tıklayın
7. API anahtarınızı kopyalayın

---

## 🚀 Uygulamayı Kullanma

### Uygulamayı Açtıktan Sonra

1. **Sol taraftaki Ayarlar Panelinden:**
   - API anahtarınızı girin (ilk kez)
   - Sistem promptunu özelleştirin (isteğe bağlı)

2. **Sohbet Başlat:**
   - "Mesajınızı yazın..." alanına bir mesaj yazın
   - "📤 Gönder" butonuna tıklayın
   - Jarvis'in yanıtını bekleyin

3. **Sistem Komutları:**
   - "Saat kaç?" → Mevcut saati gösterir
   - "Bugünün tarihi nedir?" → Tarihi gösterir
   - "Sistem bilgisi" → Sistem hakkında bilgi verir

---

## ❓ Sık Sorulan Sorular

**S: "API Anahtarı yapılandırılmadı" hatası alıyorum**
C: Sidebar'dan API anahtarınızı girin veya `.env` dosyasını kontrol edin.

**S: Parçacık animasyonu görünmüyor**
C: Tarayıcınızın JavaScript'i etkin olduğundan emin olun. Sayfayı yenileyin.

**S: Mesajlar gönderilmiyor**
C: İnternet bağlantınızı kontrol edin. OpenRouter hesabınızda kredi olduğundan emin olun.

**S: iPhone'da çalışmıyor**
C: Streamlit Cloud'a yayınladığınızdan emin olun. Lokal bilgisayardan çalışan uygulamaya iPhone'dan erişemezsiniz.

---

## 📞 Destek

Herhangi bir sorun yaşarsanız, lütfen GitHub Issues'da bir rapor oluşturun veya benimle iletişime geçin.

---

**Jarvis'i Kullan ve Keyif Al! 🚀**
