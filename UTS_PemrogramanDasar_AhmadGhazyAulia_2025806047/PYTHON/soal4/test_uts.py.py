"""
test_uts.py — Unit test sederhana untuk Soal 3 & 4 (pytest)
Jalankan: pytest test_uts.py -v
"""
import sys, os

# agar bisa import modul dari subfolder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "soal3"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "soal4"))

from utils import (
    hitung_baris, hitung_kata,
    frekuensi_kata, hitung_vokal_konsonan,
)


# ─────────────── SOAL 3 ───────────────
class TestHitungBaris:
    def test_baris_normal(self):
        assert hitung_baris("baris satu\nbaris dua\nbaris tiga") == 3

    def test_baris_kosong(self):
        assert hitung_baris("") == 1   # splitlines("") == [""]

    def test_baris_satu(self):
        assert hitung_baris("hanya satu baris") == 1


class TestHitungKata:
    def test_kata_normal(self):
        assert hitung_kata("python adalah bahasa pemrograman") == 4

    def test_kata_kosong(self):
        assert hitung_kata("") == 0

    def test_kata_spasi_ganda(self):
        assert hitung_kata("satu  dua   tiga") == 3


class TestFrekuensiKata:
    def test_top1(self):
        teks = "python python python belajar belajar"
        top = frekuensi_kata(teks, top_n=1)
        assert top[0][0] == "python"
        assert top[0][1] == 3

    def test_stopword_dihilangkan(self):
        teks = "yang dan di python python"
        top = frekuensi_kata(teks, top_n=5)
        kata = [k for k, _ in top]
        assert "yang" not in kata
        assert "python" in kata


class TestVokalKonsonan:
    def test_vokal_konsonan_basic(self):
        v, k = hitung_vokal_konsonan("python")
        assert v == 1   # 'o'
        assert k == 5   # p, y, t, h, n

    def test_hanya_angka_dan_spasi(self):
        v, k = hitung_vokal_konsonan("123 456")
        assert v == 0
        assert k == 0


# ─────────────── SOAL 4 ───────────────
class TestKonversiCSV:
    def test_baca_csv_sukses(self, tmp_path):
        """Pastikan baca_csv menghasilkan list dict yang benar."""
        import importlib.util, types

        # Buat file CSV sementara
        csv_file = tmp_path / "test.csv"
        csv_file.write_text(
            "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n"
            "Rina,2310001,80,85,90,85.50,A\n"
            "Doni,2310002,60,55,70,62.50,C\n"
        )

        # Import modul soal4
        spec = importlib.util.spec_from_file_location(
            "soal4",
            os.path.join(os.path.dirname(__file__), "soal4", "soal4_konversi.py"),
        )
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)

        data = m.baca_csv(str(csv_file))
        assert len(data) == 2
        assert data[0]["nama"] == "Rina"
        assert data[0]["nilai_akhir"] == 85.50
        assert data[1]["mutu"] == "C"

    def test_rata_rata(self, tmp_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "soal4",
            os.path.join(os.path.dirname(__file__), "soal4", "soal4_konversi.py"),
        )
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)

        data = [
            {"nilai_akhir": 80.0},
            {"nilai_akhir": 60.0},
            {"nilai_akhir": 70.0},
        ]
        rata = m.hitung_rata_rata(data)
        assert abs(rata - 70.0) < 0.001
