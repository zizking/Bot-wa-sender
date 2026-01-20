#!/bin/bash

echo "Mengupdate sistem..."
sudo apt update

echo "Menginstal Python 3 dan Pip..."
sudo apt install -y python3 python3-pip

echo "Menginstal semua library yang dibutuhkan..."
if [ -f requirements.txt ]; then
    pip install -r requirements.txt pip install -r requirements.txt --break-system-packages
else
    echo "Peringatan: file requirements.txt tidak ditemukan!"
fi

echo "Instalasi selesai! Gunakan 'python3 main.py' untuk menjalankan bot."
