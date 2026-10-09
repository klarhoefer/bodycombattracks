from collections.abc import Iterable

from .tracks import Track


def quote(value: str) -> str:
    """Maskiert einen String als MySQL-Literal."""
    escaped = value.replace("\\", "\\\\").replace("'", "''")
    return f"'{escaped}'"


def insert_statements(tracks: Iterable[Track]) -> list[str]:
    """INSERT-Statements für die Tabellen `tracks` und `durations`."""
    statements = []
    for t in tracks:
        statements.append(
            "INSERT INTO `tracks` (`releaseID`, `trackID`, `title`, `artist`) "
            f"VALUES ({t.release}, {t.number}, {quote(t.title)}, {quote(t.artist)});"
        )
        statements.append(
            "INSERT INTO `durations` (`releaseID`, `trackID`, `seconds`) "
            f"VALUES ({t.release}, {t.number}, {t.duration});"
        )
    return statements
