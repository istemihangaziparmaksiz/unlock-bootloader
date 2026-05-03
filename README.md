<div align="center">

# 🔓 Bootloader Unlocker by #ISTMHN

**A modern, GUI-based, offline MediaTek (MTK) Bootloader Unlock/Lock Tool for Windows.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-darkgreen.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Backend](https://img.shields.io/badge/Backend-MTKClient-orange.svg)](https://github.com/bkerler/mtkclient)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6.svg?logo=windows&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

</div>

---

## 🚀 Proje Hakkında (About the Project)

**Bootloader Unlocker**, MediaTek işlemcili (MTK) cihazların Bootloader kilidini açma (Unlock) ve kapatma (Lock) işlemlerini BROM (BootROM) modu üzerinden, komut satırıyla uğraşmadan yapabilmenizi sağlayan modern ve kullanıcı dostu bir araçtır. 

Sadece Redmi Note 9 (Merlin) değil, **MTKClient'ın desteklediği tüm MediaTek cihazlarla** tam uyumlu çalışacak şekilde tasarlanmıştır.

Arka planda [MTKClient](https://github.com/bkerler/mtkclient) altyapısını kullanır, ancak bu karmaşık yapıyı gizleyerek size şık ve donmayan (Thread-safe) bir arayüz sunar. Tamamen **Offline (Çevrimdışı)** çalışır.

---

## ✨ Özellikler (Features)

- 🎨 **Modern ve Koyu Tema (Dark Mode)**: `CustomTkinter` kullanılarak tasarlandı.
- ⚡ **Otomatik BROM Algılama**: Cihazı BROM modunda bağladığınız an otomatik olarak işlemlere başlar.
- 🛡️ **Güvenli İşlem Durdurma**: Yanlış bir işlem başlattığınızda **"İŞLEMİ DURDUR"** butonuna basarak işlemleri `taskkill` yöntemiyle anında kesebilir ve portu serbest bırakabilirsiniz.
- 📦 **Tek Dosya (OneFile) Mimari**: Setup programlarına gömülmeye hazır! İçerisinde kendi Python ortamı, MTKClient kütüphaneleri ve UsbDk sürücülerini barındıran tek bir `.exe` olarak çalışır. İnternet veya Python kurulumu gerektirmez.
- 📝 **Türkçe ve Okunabilir Loglar**: Karmaşık terminal kodları yerine *"Cihaz algılandı, handshake başarılı"* gibi net ve anlaşılır bildirimler sunar.

---

## 🛠️ Desteklenen Cihazlar

Bu yazılım arka planda evrensel `da seccfg unlock/lock` komutlarını kullanır. Bu komutların çalıştığı, **güvenliği yamalanmamış (Unpatched SLA/DAA)** tüm MTK cihazlarda çalışır.
- Xiaomi / Redmi (Örn: Redmi Note 9, Redmi 9, Note 8 Pro vb.)
- POCO (Örn: POCO M3 Pro vb.)
- MediaTek işlemcili desteklenen diğer marka cihazlar.

---

## 📥 Kurulum ve Derleme (Installation & Build)

Projeyi kendi bilgisayarınızda derlemek istiyorsanız şu adımları izleyin:

1. **Python 3.11+** yüklü olduğundan emin olun.
2. Repoyu klonlayın ve klasöre girin:
   ```bash
   git clone https://github.com/istemihangaziparmaksiz/unlock-bootloader.git
   cd unlock-bootloader
   ```
3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
   *(Not: `requirements.txt` dosyası resmi `mtkclient` kütüphanesini GitHub üzerinden çeker)*
4. `drivers/` klasörüne `UsbDk_1.0.22_x64.msi` isimli sürücü kurulum dosyasını ekleyin (veya `install_driver.bat` içeriğini kendi sürücünüze göre ayarlayın).
5. Kendi mavi ikonunuzu (`app_icon.ico`) oluşturmak için:
   ```bash
   python create_icon.py
   ```
6. **Derleyin**:
   ```bash
   build.bat
   ```
   Çıktı `dist/MTK_Bootloader_Unlocker.exe` olarak hazır olacaktır!

---

## 🎮 Kullanım (Usage)

1. `MTK_Bootloader_Unlocker.exe` dosyasını yönetici olarak çalıştırın.
2. Bilgisayarınızda MTK sürücüleri yoksa sol menüden **"Sürücü Kur"** butonuna basın ve kurulumun sessizce bitmesini bekleyin.
3. **"Bootloader Kilidini Aç"** veya **"Bootloader Kilidini Kapat"** butonlarından birine tıklayın.
4. Cihazınızı **tamamen kapatın**.
5. Cihazın **Ses Açma + Ses Kısma** tuşlarına basılı tutarak USB kablosunu bilgisayara takın.
6. Sağ taraftaki log ekranında *"Bootloader kilidi başarıyla açıldı"* yazısını görene kadar bekleyin.

---

## ⚠️ Yasal Uyarı (Disclaimer)

Bu araç tamamen eğitim ve kurtarma amaçlı geliştirilmiştir. 
- Bootloader kilidini açmak cihazınızı garanti kapsamı dışına çıkarabilir.
- Bootloader kilidi açma veya kapama işlemi cihazınızdaki **TÜM VERİLERİN SİLİNMESİNE (Factory Reset)** yol açar! Lütfen işlemden önce verilerinizi yedekleyin.
- Cihazınızda oluşabilecek brick (çökme) veya donanımsal arızalardan geliştirici (#ISTMHN) sorumlu tutulamaz. Tüm sorumluluk kullanıcıya aittir.

---
*Developed with ❤️ by [#ISTMHN](https://github.com/istemihangaziparmaksiz)*
