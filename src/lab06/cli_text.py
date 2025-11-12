import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        p = Path(args.input)
        if not p.exists():
            raise FileNotFoundError("Файл не найден")
        with p.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.rstrip("\n")
                if args.n:
                    print(f"{i}\t{line}")
                else:
                    print(line)

    elif args.command == "stats":
        p = Path(args.input)
        if not p.exists():
            raise FileNotFoundError("Файл не найден")
        text = p.read_text(encoding="utf-8")
        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)
        for word, count in top_n(freq, args.top):
            print(f"{word}:{count}")

if __name__ == "__main__":
    main()
