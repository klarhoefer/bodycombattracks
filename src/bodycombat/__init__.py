import argparse
from pathlib import Path

from .tracks import parse_tracks


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Liest einen iTunes-Export (Textdatei) mit den Tracks eines BODYCOMBAT-Releases."
    )
    parser.add_argument("file", type=Path, help="iTunes-Exportdatei (UTF-16, tabgetrennt)")
    parser.add_argument("release", type=int, help="Nummer des Releases, z. B. 108")
    args = parser.parse_args(argv)

    for t in parse_tracks(args.file, args.release):
        minutes, seconds = divmod(t.duration, 60)
        print(f"{t.release}/{t.number:02d} {t.title} - {t.artist} ({minutes}:{seconds:02d})")
