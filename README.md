# Jarvis AI - Streamlit Web Uygulaması

Jarvis, OpenRouter API kullanarak yazılı ve sesli sohbet edebilen, sistem kontrolü yapabilen ve uzay siyahı temalı bir yapay zeka asistanının web versiyonudur. Bu uygulama, **iPhone, Android ve masaüstü tarayıcılarında** sorunsuz çalışır.

## Özellikler

- **Yazılı Sohbet:** OpenRouter API (opentroter/free modeli) ile gerçek zamanlı AI sohbeti
- **Uzay Siyahı Tema:** Göz dostu, modern ve profesyonel görünüm
- **Dinamik Parçacık Animasyonu:** Konuşma sırasında titreşen dairesel parçacık kümesi
- **Sistem Kontrolleri:** Saat, tarih ve sistem bilgilerine anlık erişim
- **Özel Sistem Promptları:** Jarvis'in davranışını anında özelleştirme
- **Mobil Uyumlu:** Tüm cihazlarda tam ekran deneyimi
- **Kolay Kurulum:** Streamlit Cloud'da ücretsiz yayınlama

## Kurulum

### 1. Gereksinimler

- Python 3.8+
- pip (Python paket yöneticisi)

### 2. Dosyaları İndir

Proje dosyalarını bilgisayarınıza indirin ve klasöre girin:

```bash
cd jarvis_streamlit_app
```

### 3. Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

### 4. OpenRouter API Anahtarını Yapılandır

**Seçenek A: .env Dosyası Kullanarak (Önerilen)**

1. Proje klasöründe `.env` adlı bir dosya oluşturun
2. Aşağıdaki satırı ekleyin:
   ```
   OPENROUTER_API_KEY=sk-or-your-api-key-here
   ```
3. `sk-or-your-api-key-here` kısmını kendi API anahtarınızla değiştirin

**Seçenek B: Uygulamada Girin**

Uygulamayı başlattıktan sonra sol taraftaki sidebar'dan API anahtarınızı girin.

### 5. Uygulamayı Çalıştır

```bash
streamlit run app.py
```

Uygulama otomatik olarak tarayıcınızda açılacak (`http://localhost:8501`).

## iPhone'a Ekleme

### Adım 1: Uygulamayı Streamlit Cloud'a Yayınla

1. GitHub hesabınız yoksa oluşturun
2. Proje dosyalarını GitHub'a yükleyin
3. [Streamlit Cloud](https://streamlit.io/cloud) adresine gidin
4. "New app" seçeneğini tıklayın
5. GitHub repository'nizi seçin ve `app.py` dosyasını belirtin
6. "Deploy" butonuna basın

### Adım 2: iPhone'a Ana Ekrana Ekle

1. Safari'de Streamlit Cloud linkini açın
2. Alttaki **Paylaş** simgesine (yukarı ok) dokunun
3. **Ana Ekrana Ekle** seçeneğini seçin
4. Uygulama adını girin ve **Ekle** butonuna basın

Artık ana ekranınızda Jarvis ikonu olacak ve dokunduğunuzda tam ekran uygulaması açılacak.

## Android'e Ekleme

1. Chrome tarayıcısında Streamlit Cloud linkini açın
2. Sağ üstteki **⋮** (üç nokta) menüsünü açın
3. **Ana ekrana yükle** seçeneğini tıklayın
4. Uygulama adını girin ve **Yükle** butonuna basın

## Masaüstünde Çalıştırma

### Windows

```bash
python -m streamlit run app.py
```

### macOS / Linux

```bash
streamlit run app.py
```

## Yapılandırma

### Sistem Promptunu Özelleştir

Uygulamayı açtıktan sonra sol taraftaki **Ayarlar** panelinden Jarvis'in davranışını değiştirebilirsiniz. Örneğin:

- "Senin adın Doktor. Tıbbi sorulara cevap ver."
- "Senin adın Kod Uzmanı. Programlama sorularına yardım et."

### API Anahtarı Alma

1. [OpenRouter](https://openrouter.ai) adresine gidin
2. Hesap oluşturun veya giriş yapın
3. Dashboard'dan API anahtarınızı kopyalayın
4. Uygulamaya yapıştırın

## Sorun Giderme

### "API Anahtarı yapılandırılmadı" Hatası

- Sidebar'dan API anahtarınızı girin veya `.env` dosyasını kontrol edin

### Parçacık Animasyonu Görünmüyor

- Tarayıcınızın JavaScript'i etkin olduğundan emin olun
- Sayfayı yenileyin (F5)

### Mesajlar Gönderilmiyor

- İnternet bağlantınızı kontrol edin
- API anahtarınızın geçerli olduğundan emin olun
- OpenRouter hesabınızda yeterli kredi olduğundan emin olun

## Dosya Yapısı

```
jarvis_streamlit_app/
├── app.py                 # Ana Streamlit uygulaması
├── config.py              # Yapılandırma dosyası
├── requirements.txt       # Python bağımlılıkları
├── .streamlit/
│   └── config.toml       # Streamlit yapılandırması
├── .env.example          # Çevre değişkenleri örneği
└── README.md             # Bu dosya
```

## Teknoloji Stack

- **Streamlit:** Web arayüzü
- **OpenRouter API:** AI modelleri
- **Python:** Backend mantığı
- **HTML/CSS/JavaScript:** Parçacık animasyonu

## Lisans

Bu proje açık kaynaktır ve özgürce kullanılabilir.

## Destek

Herhangi bir sorun yaşarsanız, lütfen GitHub Issues'da bir rapor oluşturun.

---

**Jarvis'i Kullan ve Keyif Al! 🚀**
