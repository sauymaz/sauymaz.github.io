"""Import manually maintained YOK Akademik publication data from CSV to JSON."""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "imports" / "yok-akademik" / "publications.csv"
DEFAULT_OUTPUT = ROOT / "src" / "data" / "publications.json"


def parse_bool(value: str) -> bool:
    return value.strip().lower() in {"true", "yes", "1", "y"}


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8-sig", newline="") as handle:
        records = []
        for row in csv.DictReader(handle):
            if not any(row.values()):
                continue
            records.append({
                "id": row["id"].strip(), "year": int(row["year"]), "type": row["type"].strip(),
                "title": row["title"].strip(), "authors": row["authors"].strip(), "venue": row["venue"].strip(),
                "volume": row["volume"].strip(), "issue": row["issue"].strip(), "pages": row["pages"].strip(),
                "doi": row["doi"].strip(), "url": row["url"].strip(), "keywords": split_values(row["keywords"]),
                "featured": parse_bool(row["featured"]), "source": row["source"].strip(),
            })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(records)} publication record(s) to {args.output}")


if __name__ == "__main__":
    main()
