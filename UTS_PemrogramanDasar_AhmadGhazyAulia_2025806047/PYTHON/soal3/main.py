"""main.py — entry point Analisis Teks Otomatis (dengan argparse)"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from analyzer import analisis, buat_laporan


def main():
    parser = argparse.ArgumentParser(
        description="Analisis Teks Otomatis — UTS Pemrograman Dasar"
    )
    parser.add_argument(
        "--file", "-f",
        default="input.txt",
        help="Path file teks yang akan dianalisis (default: input.txt)",
    )
    parser.add_argument(
        "--output", "-o",
        default="report.txt",
        help="Path file laporan output (default: report.txt)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[ERROR] File '{args.file}' tidak ditemukan.")
        sys.exit(1)

    print(f"\n  Menganalisis: {args.file} ...")
    hasil = analisis(args.file)
    buat_laporan(hasil, args.output)


if __name__ == "__main__":
    main()
