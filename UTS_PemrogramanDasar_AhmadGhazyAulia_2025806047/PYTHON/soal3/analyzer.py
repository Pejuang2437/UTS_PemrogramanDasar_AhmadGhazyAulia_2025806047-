"""analyzer.py — modul analisis utama"""
from utils import (
    baca_file, hitung_baris, hitung_kata,
    frekuensi_kata, hitung_vokal_konsonan, grafik_ascii,
)


def analisis(input_path: str) -> dict:
    teks   = baca_file(input_path)
    baris  = hitung_baris(teks)
    kata   = hitung_kata(teks)
    top5   = frekuensi_kata(teks, top_n=5)
    vokal, konsonan = hitung_vokal_konsonan(teks)

    return {
        "teks":    teks,
        "baris":   baris,
        "kata":    kata,
        "top5":    top5,
        "vokal":   vokal,
        "konsonan": konsonan,
        "grafik":  grafik_ascii(top5),
    }


def buat_laporan(hasil: dict, output_path: str) -> None:
    top5_str = "\n".join(f"  {i+1}. {k} ({v}x)" for i, (k, v) in enumerate(hasil["top5"]))
    laporan = f"""
=======================================================
           LAPORAN ANALISIS TEKS OTOMATIS
=======================================================

📄 STATISTIK UMUM
  Jumlah baris : {hasil['baris']}
  Jumlah kata  : {hasil['kata']}
  Jumlah vokal : {hasil['vokal']}
  Jumlah konsonan : {hasil['konsonan']}

🏆 5 KATA PALING SERING MUNCUL
{top5_str}

📊 GRAFIK FREKUENSI KATA
{hasil['grafik']}

=======================================================
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(laporan.strip() + "\n")
    print(laporan)
    print(f"  ✔ Laporan disimpan ke: {output_path}")
