# Tartım İstasyonu Simülasyonu: Kullanım

Tek sayfalık 3D/VR simülasyon (`index.html`). Kabin, Higgsfield referans fotoğrafındaki gibi kompakt kuruldu: 3,2 × 2,8 m, tavan 2,6 m. Depodan ön cephedeki çift kanatlı kapıyla girilir; açılış görüntüsü referans fotoğrafla aynı açıdan bakar.

- `assets/models/`: gerçek 3D modeller. Zemin terazisi, hassas terazi, barkod yazıcı, barkod okuyucu, panel PC, terazi göstergesi, kovalar, kavanoz, çuval, palet, raf ve sehpa Higgsfield SAM 3D ile; paslanmaz masa Hugging Face TRELLIS ile üretildi (kaynak ürün çekimleri: Gemini). Operatör karakteri Tripo ile modellenip Meshy ile iskeletlendi (`operator.glb`).
- Işık: tavandaki 4 LED panel alan ışığı olarak aydınlatır; paslanmaz yüzeyler ve epoksi zemin, açılışta bir kez çekilen kabin içi yansıma haritasını kullanır. Zemin yansıması yalnız masaüstünde açıktır, VR'da performans için kapanır.
- `assets/tex/`: duvar, zemin, çelik, kraft, ahşap, Tyvek vb. dokular ve fabrika panoraması (Higgsfield).
- `assets/gemini/`: Gemini ile üretilen sahne görselleri ve ürün çekimleri. Yalnız kaynak; simülasyon kullanmadığı için GitHub deposunda yok.
- `assets/v*.mp4`: tanıtım filmi klipleri (Higgsfield).

## Modlar

- **Senaryoyu izle**: 19 adımlık sinematik anlatım. Operatör karakteri defterdeki senaryoyu baştan sona uygular: lot seçimi, yanlış çuval ikazı, Terazi 1'de dara, tartım ve tolerans kontrolü, etiket, teyit, MIRA kaydı, hassas terazide yanlış terazi ve tolerans dışı uyarısı, streç, QR. Oynat/duraklat, adım atlama, hız (0,75–2×) ve serbest kamera var. Türkçe ses paketi kuruluysa adımlar sesli okunur.
- **Operatör olarak uygula**: birinci şahıs. İşi kullanıcı kendisi yapar. Ekrandaki görev listesi ve turuncu ok bir sonraki adımı gösterir. İlk iki kalemden sonra kalanlar ekrandan otomatik tamamlanabilir.
- **Tanıtım filmi**: 5 Higgsfield klibi art arda oynar (sunum açılışı için).

## Kontroller

| | Masaüstü | Meta Quest |
|---|---|---|
| Bak | Sürükle (veya "Fareyi kilitle") | Baş hareketi |
| Yürü | WASD | Sol çubuk |
| Dön | Sürükle | Sağ çubuk (30°) |
| Işınlan | Zemindeki mavi halkaya tıkla | Halkaya doğrult + tetik |
| Kullan / okut | Sol tık | Tetik |
| Dök | Ürünü tutarken kaba bakıp sol tuşu basılı tut | Ürünü kabın üstünde tutup tetiği basılı tut veya eğ |
| Al / bırak | Sağ tık veya E | Grip (yan tuş) |

## Meta Quest'te açmak

1. Bilgisayar ve Quest aynı Wi-Fi ağında olsun.
2. `Quest_icin_baslat.bat` dosyasına çift tıklayın. Windows güvenlik duvarı sorarsa "Özel ağ" için izin verin.
3. Pencerede yazan adresi (örnek: `https://192.168.1.9:8443`) Quest tarayıcısında açın.
4. "Bağlantınız gizli değil" uyarısında **Gelişmiş > Devam et** deyin. Sertifika yerel olarak üretildi; bu uyarı beklenen bir durum.
5. **Operatör olarak uygula** (veya Senaryoyu izle) > **VR'da aç**.

Alternatif (geliştirici modu açık Quest + USB kablo): `adb reverse tcp:8765 tcp:8765` komutundan sonra Quest'te `http://localhost:8765` açılabilir.

İnternet bağlantısı gerekir: Three.js, fontlar ve kumanda modelleri CDN'den yüklenir.

## Not

Senaryo sırasında batch paleti kabin kapısının sağında, depo (çuvallar, kavanozlar, raflar) solundadır.

Reçete, lot ve ağırlık değerleri (LOT 26-1042, RC-0417, 25,000 kg ± 0,050 vb.) örnek değerlerdir. Gerçek değerler `index.html` içindeki `ITEMS0` dizisinden değiştirilebilir.
