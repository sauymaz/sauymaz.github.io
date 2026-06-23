"""Import manually maintained academic experience data from CSV to JSON."""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "imports" / "yok-akademik" / "academic-experience.csv"
DEFAULT_OUTPUT = ROOT / "src" / "data" / "academic-experience.json"


def optional_year(value: str) -> int | None:
    value = value.strip()
    return int(value) if value else None


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
                "id": row["id"].strip(), "title": row["title"].strip(),
                "institution": row["institution"].strip(), "faculty": row["faculty"].strip(),
                "department": row["department"].strip(), "unit": row["unit"].strip(),
                "startYear": optional_year(row["startYear"]), "endYear": optional_year(row["endYear"]),
                "type": row["type"].strip(), "description": row["description"].strip(),
            })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(records)} academic experience record(s) to {args.output}")


if __name__ == "__main__":
    main()
