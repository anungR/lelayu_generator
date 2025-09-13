# generate_qr.py
# Script untuk membuat QR code ke halaman GitHub Pages lelayu_pak_sinung

import qrcode

# URL GitHub Pages (pastikan sudah rename index.html)
URL = "https://anungr.github.io/lelayu_pak_sinung/"

# Membuat objek QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Kualitas tinggi
    box_size=10,  # Ukuran kotak
    border=4,     # Border sekitar QR
)

# Menambahkan data URL ke QR
qr.add_data(URL)
qr.make(fit=True)

# Membuat gambar QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Simpan ke file PNG
img.save("qrcode_lelayu.png")

print(f"QR code berhasil dibuat! File disimpan sebagai qrcode_lelayu.png")
