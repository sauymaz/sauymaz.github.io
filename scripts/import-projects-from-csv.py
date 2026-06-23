"""Import manually maintained YOK Akademik project data from CSV to JSON."""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "imports" / "yok-akademik" / "projects.csv"
DEFAULT_OUTPUT = ROOT / "src" / "data" / "projects.json"


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
                "id": row["id"].strip(), "title": row["title"].strip(), "role": row["role"].strip(),
                "category": row["category"].strip(), "fundingBody": row["fundingBody"].strip(),
                "year": row["year"].strip(), "status": row["status"].strip(),
                "description": row["description"].strip(), "keywords": split_values(row["keywords"]),
                "outputs": split_values(row["outputs"]), "url": row["url"].strip(),
                "featured": parse_bool(row["featured"]), "source": row["source"].strip(),
            })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(records)} project record(s) to {args.output}")


if __name__ == "__main__":
    main()
