import argparse
from pathlib import Path

from .sql import insert_statements
from .tracks import parse_tracks


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Liest einen iTunes-Export (Textdatei) mit den Tracks eines BODYCOMBAT-Releases."
    )
    parser.add_argument("file", type=Path, help="iTunes-Exportdatei (UTF-16, tabgetrennt)")
    parser.add_argument("release", type=int, help="Nummer des Releases, z. B. 108")
    parser.add_argument(
        "--sql", action="store_true", help="Tracks als SQL-INSERT-Statements in eine .sql-Datei neben der Eingabedatei schreiben"
    )
    args = parser.parse_args(argv)

    tracks = parse_tracks(args.file, args.release)
    if args.sql:
        target = args.file.with_suffix(".sql")
        target.write_text("\n".join(insert_statements(tracks)) + "\n", encoding="utf-8")
        print(f"{len(tracks)} Tracks nach {target} geschrieben")
        return

    for t in tracks:
        minutes, seconds = divmod(t.duration, 60)
        print(f"{t.release}/{t.number:02d} {t.title} - {t.artist} ({minutes}:{seconds:02d})")
