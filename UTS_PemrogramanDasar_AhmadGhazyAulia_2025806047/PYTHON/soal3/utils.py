"""utils.py — fungsi bantu analisis teks"""
import re
from collections import Counter

STOPWORDS = {
    "yang", "dan", "di", "ke", "dari", "ini", "itu", "adalah", "dengan",
    "untuk", "pada", "atau", "juga", "dalam", "tidak", "akan", "dapat",
    "oleh", "kita", "ada", "sebagai", "sebuah", "serta", "bisa", "sudah",
    "telah", "kami", "mereka", "nya", "si", "pun", "agar", "namun",
    "karena", "seperti", "atas", "bagi", "ia", "lebih", "kini", "hal",
    "the", "a", "an", "is", "in", "of", "to", "and", "for", "it",
}

VOKAL = set("aeiouAEIOU")


def baca_file(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def hitung_baris(teks: str) -> int:
    return len(teks.splitlines())


def hitung_kata(teks: str) -> int:
    return len(teks.split())


def frekuensi_kata(teks: str, top_n: int = 5) -> list[tuple[str, int]]:
    kata_bersih = re.findall(r"[a-zA-Z]+", teks.lower())
    kata_filter = [k for k in kata_bersih if k not in STOPWORDS and len(k) > 2]
    return Counter(kata_filter).most_common(top_n)


def hitung_vokal_konsonan(teks: str) -> tuple[int, int]:
    vokal = sum(1 for c in teks if c in VOKAL)
    konsonan = sum(1 for c in teks if c.isalpha() and c not in VOKAL)
    return vokal, konsonan


def grafik_ascii(freq: list[tuple[str, int]], lebar: int = 30) -> str:
    if not freq:
        return ""
    maks = freq[0][1]
    baris = []
    for kata, jml in freq:
        panjang_bar = int((jml / maks) * lebar)
        bar = "█" * panjang_bar
        baris.append(f"  {kata:<15} {bar} ({jml})")
    return "\n".join(baris)
