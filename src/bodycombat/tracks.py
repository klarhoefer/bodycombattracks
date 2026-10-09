import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Track:
    number: int
    title: str
    artist: str
    duration: int  # Sekunden


def parse_tracks(path: str | Path) -> list[Track]:
    """Liest einen iTunes-Export (UTF-16, tabgetrennt) als Liste von Tracks."""
    with open(path, encoding="utf-16", newline="") as f:
        rows = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        return [
            Track(
                number=int(row["Titelnummer"]),
                title=row["Titelname"],
                artist=row["Künstler"],
                duration=int(row["Dauer"]),
            )
            for row in rows
        ]
