"""scoreboard.py — manajemen skor pemain (file scores.json)"""
import json
import os

SCORES_FILE = os.path.join(os.path.dirname(__file__), "scores.json")


def load_scores() -> list:
    if not os.path.exists(SCORES_FILE):
        return []
    try:
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_score(name: str, score: int) -> None:
    scores = load_scores()
    # Update jika pemain sudah ada, simpan skor tertinggi
    for entry in scores:
        if entry["name"].lower() == name.lower():
            if score > entry["score"]:
                entry["score"] = score
            return _write(scores)
    scores.append({"name": name, "score": score})
    _write(scores)


def _write(scores: list) -> None:
    scores.sort(key=lambda x: x["score"], reverse=True)
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def show_top5(color) -> None:
    scores = load_scores()
    print(color.CYAN + "\n  ╔══════════════════════╗" + color.RESET)
    print(color.CYAN + "  ║    TOP 5 SCOREBOARD  ║" + color.RESET)
    print(color.CYAN + "  ╚══════════════════════╝" + color.RESET)
    if not scores:
        print(color.YELLOW + "  Belum ada skor tersimpan." + color.RESET)
        return
    medals = ["🥇", "🥈", "🥉", "4.", "5."]
    for i, entry in enumerate(scores[:5]):
        bar = "█" * (entry["score"] // 10)
        print(color.GREEN + f"  {medals[i]} {entry['name']:<15} {entry['score']:>4} pts  {bar}" + color.RESET)
    print()
