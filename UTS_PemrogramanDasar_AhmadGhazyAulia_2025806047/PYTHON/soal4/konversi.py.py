"""
soal4_konversi.py
Membaca data_mahasiswa.csv (output program C Soal 1),
menampilkan data dengan rapi, menghitung rata-rata nilai akhir,
dan mengonversi ke data_mahasiswa.json.

Jalankan:
    python soal4_konversi.py
atau dengan path custom:
    python soal4_konversi.py --csv ../../C/data_mahasiswa.csv
"""

import csv
import json
import argparse
import os
import sys


def baca_csv(path: str) -> list[dict]:
    """Baca CSV dan kembalikan list dict."""
    if not os.path.exists(path):
        print(f"[ERROR] File tidak ditemukan: {path}")
        sys.exit(1)

    data = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                "nama":        row["Nama"],
                "nim":         row["NIM"],
                "tugas":       float(row["Tugas"]),
                "uts":         float(row["UTS"]),
                "uas":         float(row["UAS"]),
                "nilai_akhir": float(row["NilaiAkhir"]),
                "mutu":        row["Mutu"],
            })
    return data


def tampilkan_tabel(data: list[dict]) -> None:
    """Tampilkan data mahasiswa dalam format tabel rapi."""
    print("\n" + "=" * 70)
    print("           DATA MAHASISWA — HASIL KONVERSI CSV")
    print("=" * 70)
    header = f"  {'Nama':<18} {'NIM':<12} {'Tugas':>6} {'UTS':>6} {'UAS':>6} {'Akhir':>8} {'Mutu':>5}"
    print(header)
    print("  " + "-" * 66)
    for m in data:
        print(f"  {m['nama']:<18} {m['nim']:<12} {m['tugas']:>6.1f} {m['uts']:>6.1f}"
              f" {m['uas']:>6.1f} {m['nilai_akhir']:>8.2f} {m['mutu']:>5}")
    print("  " + "-" * 66)


def hitung_rata_rata(data: list[dict]) -> float:
    if not data:
        return 0.0
    return sum(m["nilai_akhir"] for m in data) / len(data)


def simpan_json(data: list[dict], path: str) -> None:
    """Simpan hanya field relevan ke JSON."""
    output = [
        {
            "nama":        m["nama"],
            "nim":         m["nim"],
            "nilai_akhir": m["nilai_akhir"],
            "mutu":        m["mutu"],
        }
        for m in data
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\n  ✔ Data berhasil disimpan ke: {path}")
    print("\n  Contoh isi JSON:")
    print(json.dumps(output[:2], indent=4, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Konversi data_mahasiswa.csv → JSON")
    parser.add_argument("--csv",  default=os.path.join(os.path.dirname(__file__),
                                                        "../../C/data_mahasiswa.csv"),
                        help="Path file CSV input")
    parser.add_argument("--json", default=os.path.join(os.path.dirname(__file__),
                                                        "data_mahasiswa.json"),
                        help="Path file JSON output")
    args = parser.parse_args()

    csv_path  = os.path.abspath(args.csv)
    json_path = os.path.abspath(args.json)

    print(f"\n  Membaca: {csv_path}")
    data = baca_csv(csv_path)

    tampilkan_tabel(data)

    rata = hitung_rata_rata(data)
    print(f"\n  📊 Rata-rata Nilai Akhir : {rata:.2f}")
    print(f"  📦 Total mahasiswa       : {len(data)}")

    simpan_json(data, json_path)


if __name__ == "__main__":
    main()
