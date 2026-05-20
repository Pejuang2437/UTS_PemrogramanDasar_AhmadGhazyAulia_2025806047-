"""game.py — logika inti permainan Guess Battle"""
import random

LEVELS = {
    1: {"range": (1, 10),  "tries": 3},
    2: {"range": (1, 50),  "tries": 5},
    3: {"range": (1, 100), "tries": 7},
}


def play_level(level: int, color) -> int:
    """Mainkan satu level. Kembalikan skor (0 jika kalah)."""
    cfg        = LEVELS[level]
    lo, hi     = cfg["range"]
    max_tries  = cfg["tries"]
    secret     = random.randint(lo, hi)
    tries_left = max_tries

    print(color.CYAN + f"\n  ★ LEVEL {level} — Tebak angka {lo}–{hi} | {max_tries} percobaan" + color.RESET)

    while tries_left > 0:
        print(color.YELLOW + f"  Sisa percobaan: {tries_left}" + color.RESET, end="  ")
        try:
            guess = int(input(color.WHITE + "Tebakan kamu: " + color.RESET))
        except ValueError:
            print(color.RED + "  ⚠  Masukkan angka yang valid!" + color.RESET)
            continue

        if guess == secret:
            score = tries_left * 10 * level
            print(color.GREEN + f"  ✔  Benar! +{score} poin" + color.RESET)
            return score
        elif guess < secret:
            print(color.MAGENTA + "  ↑  Terlalu kecil!" + color.RESET)
        else:
            print(color.MAGENTA + "  ↓  Terlalu besar!" + color.RESET)

        tries_left -= 1

    print(color.RED + f"  ✘  Kehabisan percobaan! Angkanya adalah {secret}." + color.RESET)
    return 0


def play_game(player_name: str, color) -> int:
    """Jalankan semua level dan kembalikan total skor."""
    total = 0
    for lvl in (1, 2, 3):
        total += play_level(lvl, color)
    print(color.CYAN + f"\n  Skor akhir {player_name}: {total} poin\n" + color.RESET)
    return total
