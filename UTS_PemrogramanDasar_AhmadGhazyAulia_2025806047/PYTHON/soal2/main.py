"""main.py — entry point Guess Battle"""
try:
    from colorama import Fore, Style, init
    init(autoreset=True)

    class color:
        RED     = Fore.RED
        GREEN   = Fore.GREEN
        YELLOW  = Fore.YELLOW
        CYAN    = Fore.CYAN
        MAGENTA = Fore.MAGENTA
        WHITE   = Fore.WHITE
        RESET   = Style.RESET_ALL
except ImportError:
    # Fallback tanpa warna jika colorama belum di-install
    class color:
        RED = GREEN = YELLOW = CYAN = MAGENTA = WHITE = RESET = ""

from game import play_game
from scoreboard import save_score, show_top5


def banner():
    print(color.CYAN + """
  ╔════════════════════════════════╗
  ║   🎮  GUESS BATTLE  v1.0 🎮   ║
  ║  Tema: Data, Game & Analisis  ║
  ╚════════════════════════════════╝
""" + color.RESET)


def main():
    banner()
    print(color.YELLOW + "  Selamat datang di Guess Battle!" + color.RESET)
    name = input(color.WHITE + "  Masukkan nama pemain: " + color.RESET).strip()
    if not name:
        name = "Pemain"

    again = True
    while again:
        score = play_game(name, color)
        save_score(name, score)
        show_top5(color)

        ans = input(color.YELLOW + "  Main lagi? (y/n): " + color.RESET).strip().lower()
        again = (ans == "y")

    print(color.CYAN + "\n  Terima kasih sudah bermain! Sampai jumpa 👋\n" + color.RESET)


if __name__ == "__main__":
    main()
