# 🧹 Image Cleaner (PNG Keeper)

Bu Python scripti, belirli bir klasörü izleyerek:

- `.jpg` dosyalarını `.png` formatına çevirir.
- `.png` dışında kalan dosyaları otomatik olarak siler.
- Klasöre eklenen yeni dosyaları anlık olarak işler.

---

## 🚀 Kurulum

1. Gerekli bağımlılıkları yüklemek için terminalde aşağıdaki komutu çalıştır:

```bash
pip install -r requirements.txt

⚙️ Kullanım
cleaner.py dosyasındaki WATCHED_DIR değişkenini kendi izlemek istediğiniz klasör yoluna göre değiştir:

WATCHED_DIR = r"C:\Users\kullanici_adiniz\Downloads\downthemall"
Scripti çalıştırmak için terminalde:


python cleaner.py
Artık bu klasörde .jpg dosyaları .png'ye çevrilir, diğer uzantılar silinir ve klasöre yeni dosya eklendiğinde anında işlem yapılır.


## Gerekli Kütüphaneler

- Pillow
- watchdog
