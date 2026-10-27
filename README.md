# Tartım İstasyonu Simülasyonu

GMP tartım kabininin tarayıcıda çalışan 3D/VR simülasyonu: MIRA ERP'den lot ve reçete gelişi, barkodla ürün teyidi, iki terazide dara ve tartım, etiket, batch streç ve QR. Masaüstünde ve Meta Quest'te çalışır.

Kontroller, modlar ve Quest kurulumu: [KULLANIM.md](KULLANIM.md)

## Kurulum ve açma

Gerekenler: Python 3 ve internet bağlantısı (Three.js ve fontlar CDN'den gelir). Derleme ya da paket kurulumu yok.

```bash
git clone https://github.com/omerfarukbilen/tartim-simulasyonu.git
cd tartim-simulasyonu
python -m http.server 8000
```

Sonra tarayıcıda `http://localhost:8000` adresini açın. Windows'ta `python` bulunamazsa `py -m http.server 8000` kullanın. Port 8000 doluysa başka bir port (ör. 8080) verip adresi ona göre açın. Sunucuyu kapatmak için Ctrl+C.

Depo private: klonlamak için makinede GitHub oturumu açık olmalı (`gh auth login`). İndirme yaklaşık 50 MB; klon diskte yaklaşık 105 MB yer kaplar.

`index.html` dosyasına çift tıklayarak açmak çalışmaz; tarayıcı modelleri `file://` üzerinden yüklemez. Mutlaka bir yerel sunucuyla açın.

## Meta Quest (VR)

VR modu HTTPS ister. Bilgisayar ve Quest aynı Wi-Fi'deyken:

```bash
pip install cryptography
python quest_sunucu.py
```

Windows'ta `Quest_icin_baslat.bat` aynı işi yapar. Pencerede yazan `https://...:8443` adresini Quest tarayıcısında açın; ayrıntılar KULLANIM.md'de.

## Claude ile kurulum

Claude'a bu depo linkini verip "kur ve aç" demeniz yeterli. Claude için adımlar: depoyu klonla, klasörde `python -m http.server 8000` komutunu arka planda başlat, tarayıcıda `http://localhost:8000` adresini aç. Sayfa açılınca intro ekranında "Senaryoyu izle" ya da "Operatör olarak uygula" seçilir.
