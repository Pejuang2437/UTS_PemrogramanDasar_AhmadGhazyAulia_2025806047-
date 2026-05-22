# 🧠 UTS Pemrograman Dasar (C & Python)

## 👤 Identitas
- Nama: [Ahmad Ghazy Aulia]
- NIM: [2025806047]
- Kelas: [Teknologi Informasi Pagi]
- Dosen: [Rintis Mahardika Sunarto]
- Repository: [https://github.com/Pejuang2437/UTS_PemrogramanDasar_AhmadGhazyAulia_2025806047-/tree/main/UTS_PemrogramanDasar_AhmadGhazyAulia_2025806047]

---

## 📚 Deskripsi
Proyek ini adalah Ujian Tengah Semester (UTS) Pemrograman Dasar, yang menggabungkan konsep C dan Python.  
Mahasiswa diminta membuat beberapa proyek terpisah dengan fitur logika, struktur data, file handling, dan modular programming.

---

## 🧩 Struktur Folder

UTS_PemrogramanDasar_AhmadGhazyAulia_2025806047/
├── C/
│   └── data_mahasiswa.c        # Soal 1 — Sistem Data Mahasiswa
├── Python/
│   ├── soal2/
│   │   ├── main.py             # Entry point Game Guess Battle
│   │   ├── game.py             # Logika permainan per level
│   │   └── scoreboard.py       # Manajemen skor (JSON)
│   ├── soal3/
│   │   ├── main.py             # Entry point Analisis Teks (argparse)
│   │   ├── analyzer.py         # Modul analisis utama
│   │   ├── utils.py            # Fungsi bantu (frekuensi, vokal, dll)
│   │   └── input.txt           # Contoh file teks input
│   ├── soal4/
│   │   ├── soal4_konversi.py   # Konversi CSV → JSON
│   │   └── data_mahasiswa.json # Output JSON (di-generate otomatis)
│   └── test_uts.py             # Unit test (pytest) — Bonus
├── docs/
│   └── (screenshot output)
└── README.md

## ⚙️ Persiapan Lingkungan

### 🔹 Instalasi C
Gunakan salah satu:
- macOS: `brew install gcc`
- Windows: install **MinGW** lalu tambahkan path ke environment
- Linux: `sudo apt install build-essential`

Cek versi:
```bash
gcc --version

🔹 Instalasi Python
Gunakan Python 3.x:
python3 --version

Jika belum ada, unduh di: https://www.python.org/downloads/
🔹 (Opsional) Buat Virtual Environment
python3 -m venv venv
source venv/bin/activate   # (macOS/Linux)
venv\Scripts\activate      # (Windows)

Instal library tambahan:
pip install colorama


🧠 Soal & Deskripsi Singkat
🧩 Soal 1 – Sistem Data Mahasiswa (C)
Menggunakan struct, pointer, linked list, file CSV


Fitur: tambah, hapus, cari, tampilkan, dan simpan data


🎮 Soal 2 – Game Tebak Angka (Python)
Fitur login pemain, level permainan, dan skor otomatis


Gunakan random, json, dan colorama


🧠 Soal 3 – Analisis Teks (Python)
Baca input.txt, hitung kata, huruf, baris, dan frekuensi kata


Tulis laporan ke report.txt


Buat modul analyzer.py dan utils.py


🔄 Soal 4 – Konversi Data (C ↔ Python)
Gunakan hasil file CSV dari Soal 1


Buat script Python untuk membaca CSV dan mengubah ke JSON



🚀 Cara Menjalankan
▶️ C (contoh Soal 1)
cd C/soal1_data_mahasiswa
gcc main.c linked_list.c -o program
./program

▶️ Python (contoh Soal 3)
cd Python/soal3_text_analyzer
python3 main.py


🧾 Laporan
Semua dokumentasi, screenshot, dan analisis ditaruh di folder /docs


Minimal berisi:


Screenshot hasil running tiap program


Analisis singkat dari tiap soal


File laporan_uts.pdf



🏁 Commit History Contoh
feat: tambah modul struct mahasiswa dan simpan ke CSV
fix: perbaiki bug pointer pada fungsi hapus data
update: tambahkan skor JSON untuk game Python
docs: tambahkan screenshot output di folder docs


📸 Contoh Output

---

## 💡 OPSIONAL: FILE `.gitignore`
Agar repo tetap bersih, buat file `.gitignore` di root:


venv/
 pycache/
 *.exe
 *.o
 *.csv
 *.json
 *.txt
 *.pdf

---
