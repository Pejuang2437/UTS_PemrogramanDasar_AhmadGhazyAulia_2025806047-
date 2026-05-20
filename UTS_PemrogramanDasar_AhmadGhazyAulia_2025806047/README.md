# UTS Pemrograman Dasar — Tema: Data, Game, dan Analisis Otomatis

> **Universitas Insan Pembangunan Indonesia — Fakultas Ilmu Komputer**  
> Mata Kuliah: Teknik Informatika | Dosen: Rintis Mardika Sunarto  
> Semester Genap 2025/2026

-----

## 👤 Identitas

|Field   |Isi              |
|--------|-----------------|
|**Nama**|`AHMAD GHAZY AULIA`|
|**NPM** |`2025806047` |

-----

## 📁 Struktur Repository

```
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
```

-----

## 📌 Penjelasan Program

### Soal 1 — Sistem Data Mahasiswa (C)

Program manajemen data mahasiswa menggunakan **linked list dinamis**.

**Fitur:**

- Input data mahasiswa (nama, NIM, nilai tugas/UTS/UAS)
- Hitung nilai akhir: `40% UAS + 30% UTS + 30% Tugas`
- Konversi nilai ke huruf mutu (A–E)
- Tampilkan tabel ke layar
- Simpan ke `data_mahasiswa.csv`
- Cari & hapus mahasiswa berdasarkan NIM
- **Bonus:** Bubble Sort berdasarkan nilai akhir

**Konsep:** struct, pointer, dynamic memory (`malloc`/`free`), file I/O

-----

### Soal 2 — Game Guess Battle (Python)

Game tebak angka berbasis multi-level dan multi-player.

**Fitur:**

- Login pemain, skor disimpan di `scores.json`
- 3 level: rentang 1–10 / 1–50 / 1–100
- Skor dihitung dari percobaan tersisa × 10 × level
- Tampilkan Top 5 pemain terbaik setelah selesai
- **Bonus:** Warna terminal (`colorama`), error handling `try-except`, modularisasi

-----

### Soal 3 — Analisis Teks Otomatis (Python)

Program menganalisis file `.txt` dan menghasilkan laporan statistik.

**Fitur:**

- Hitung jumlah baris, kata, vokal, konsonan
- Temukan 5 kata paling sering muncul (dengan filter stopword)
- Grafik frekuensi ASCII
- Output ke `report.txt`
- **Bonus:** Argparse CLI, modularisasi (`analyzer.py` + `utils.py`)

-----

### Soal 4 — Konversi Data Antar Format (C + Python)

Integrasi output C (CSV) ke Python (JSON).

**Fitur:**

- Baca `data_mahasiswa.csv` hasil program C
- Tampilkan tabel data secara rapi
- Hitung rata-rata nilai akhir semua mahasiswa
- Konversi dan simpan ke `data_mahasiswa.json`

-----

## ▶️ Instruksi Menjalankan

### Soal 1 (C)

```bash
cd C/
gcc -Wall -o data_mahasiswa data_mahasiswa.c
./data_mahasiswa
```

### Soal 2 (Python)

```bash
# Install dependency (opsional, untuk warna terminal)
pip install colorama

cd Python/soal2/
python main.py
```

### Soal 3 (Python)

```bash
cd Python/soal3/
python main.py --file input.txt --output report.txt
```

### Soal 4 (Python)

```bash
# Pastikan data_mahasiswa.csv sudah ada (run Soal 1 dulu)
cd Python/soal4/
python soal4_konversi.py --csv ../../C/data_mahasiswa.csv
```

### Unit Test — Bonus (pytest)

```bash
pip install pytest
cd Python/
pytest test_uts.py -v
```

-----

## 📊 Contoh Output

### Soal 1 — Tabel Data Mahasiswa

```
Nama                 NIM           Tugas    UTS    UAS  NilaiAkhir  Mutu
-------------------- ------------ ------ ------ ------ ---------- -----
Rina                 2310001        80.0   85.0   90.0      85.50     A
Doni                 2310002        60.0   55.0   70.0      62.50     C
Sari                 2310003        75.0   78.0   82.0      78.70     B
Bagas                2310004        90.0   88.0   95.0      91.40     A
Dewi                 2310005        55.0   60.0   65.0      60.50     C
```

### Soal 2 — Top 5 Scoreboard

```
╔══════════════════════╗
║    TOP 5 SCOREBOARD  ║
╚══════════════════════╝
🥇 Bagas           230 pts  ██████████████████████
🥈 Rina            200 pts  ████████████████████
🥉 Sari            170 pts  █████████████████
```

### Soal 3 — Grafik Frekuensi Kata

```
  python          ██████████████████████████████ (9)
  pemrograman     ████████████████████ (6)
  data            ████████████████████ (6)
  teknologi       ██████████ (3)
  banyak          ██████████ (3)
```

### Soal 4 — Output JSON

```json
[
  {"nama": "Rina",  "nim": "2310001", "nilai_akhir": 85.5, "mutu": "A"},
  {"nama": "Doni",  "nim": "2310002", "nilai_akhir": 62.5, "mutu": "C"}
]
```

-----

## 🔧 Teknologi

- **C** — GCC compiler, stdlib, stdio
- **Python 3.10+** — random, json, csv, argparse, collections, re
- **Library opsional** — colorama (warna terminal), pytest (unit test)

-----

## 📝 Catatan Commit

Urutan commit yang digunakan:

```
feat: inisialisasi struktur repo UTS
feat: tambah modul struct mahasiswa (Soal 1)
feat: implementasi linked list add delete search
feat: tambah save CSV dan bubble sort
feat: tambah game.py dan scoreboard.py (Soal 2)
feat: tambah main.py Guess Battle dengan colorama
feat: tambah analyzer.py dan utils.py (Soal 3)
feat: tambah argparse dan grafik ASCII
feat: tambah soal4_konversi CSV ke JSON
feat: tambah unit test pytest (bonus)
update: tambah README dan docs screenshot
```