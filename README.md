# 🌐 **SALDY Framework** - Panduan Lengkap

---

## 🚀 **Fitur Utama**

1. 🔓 **Bypass WAF**  
   - Bypass WAF dengan 15+ variasi payload canggih secara otomatis.

2. 🎨 **Deface Halaman Web**  
   - Mengubah tampilan halaman web target, melanjutkan meski ada endpoint yang tidak ditemukan.

3. 🔁 **Looping Serangan**  
   - Mengulang serangan pada berbagai endpoint secara otomatis.

4. ⚙️ **Konfigurasi Proxy/User-Agent**  
   - Mudah konfigurasikan proxy dan user-agent untuk serangan yang lebih aman.

5. ❌ **Keluar**  
   - Menutup framework dengan aman setelah digunakan.

---

## 📋 **Contoh Menu Framework**

```bash
========= SALDY Framework =========
1. 🔓 Bypass WAF  
2. 🎨 Deface Halaman Web  
3. 🔁 Looping Serangan  
4. ⚙️ Konfigurasi Proxy/User-Agent  
5. ❌ Keluar  

Masukkan pilihan Anda:

```
---

📌 Cara Menggunakan

1. Bypass WAF

Masukkan pilihan Anda: 1
URL Target: https://contoh-web.com
[INFO] Bypass berhasil dengan payload #8!
[INFO] Serangan dilanjutkan ke target.

2. Deface Halaman Web

Masukkan pilihan Anda: 2
URL Target: https://contoh-web.com
[INFO] Mengubah tampilan halaman di endpoint /index.html
[INFO] Endpoint lain tidak ditemukan, melanjutkan ke endpoint berikutnya.

3. Looping Serangan

Masukkan pilihan Anda: 3
[INFO] Mengulang serangan pada endpoint /login...

4. Konfigurasi Proxy/User-Agent

Masukkan pilihan Anda: 4
[INFO] Memperbarui file proxy dan user-agent...


---

📂 Struktur File

- main.py: Script utama yang mengelola seluruh proses.
- proxies.txt: Daftar proxy untuk digunakan dalam serangan.
- user_agents.txt: Daftar user-agent untuk menghindari deteksi.


---

🛠️ Cara Menjalankan Framework

Persiapan:

1. Pastikan Python sudah terinstall di sistem Anda.


2. Siapkan file proxies.txt dan user_agents.txt di direktori yang sama dengan main.py.



Jalankan Script:
```bash
python main.py
```
Ikuti instruksi yang muncul di terminal untuk melakukan pengujian keamanan.


---
