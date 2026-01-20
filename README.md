# Bot WA Sender - WhatsApp Automation 2026

Proyek ini adalah bot pengirim pesan WhatsApp otomatis yang dirancang untuk dijalankan di VPS atau komputer lokal dengan mudah.

## 📋 Prasyarat
Sebelum memulai, pastikan kamu sudah memiliki:
- Python 3.x terinstal.
- Git terinstal di sistem kamu.

---

## 🚀 Langkah Awal: Menyalin Repositori
Langkah pertama adalah mendownload kode ini ke komputer/VPS kamu. Buka terminal dan jalankan:

```bash
git clone [https://github.com/zizking/Bot-wa-sender.git](https://github.com/zizking/Bot-wa-sender.git)
cd Bot-wa-sender
```
Kamu bisa memilih salah satu dari dua cara di bawah ini:
1. Cara Otomatis (Sangat Direkomendasikan)
Gunakan skrip instalasi untuk menyiapkan seluruh sistem sekaligus:

# Berikan izin eksekusi pada file install
```bash
chmod +x install.sh
```

# Jalankan skrip instalasi
```bash
./install.sh
```
2. Cara Manual
Jika ingin melakukan instalasi langkah demi langkah, ikuti perintah berikut:
A. Update Sistem & Instal Python
```bash
sudo apt update
sudo apt install python3 python3-pip
```

B. Instal Library yang Dibutuhkan

```bash
pip install -r requirements.txt
```

Konfigurasi & Cara Menjalankan
Siapkan Data:
• Masukkan daftar nomor tujuan di file nomor.txt.
• Tulis isi pesan yang ingin dikirim di file pesan.
• Pastikan wa_login.py siap untuk proses autentikasi

2. Jalankan Bot:
```bash
python3 main.py
```



Fitur Utama
• Clone & Go: Mudah disalin dan langsung dijalankan.
• Otomatisasi Penuh: Menangani pengiriman pesan sesuai daftar nomor secara berurutan.
• Dua Mode Instalasi: Mendukung skrip bash otomatis atau langkah manual.
