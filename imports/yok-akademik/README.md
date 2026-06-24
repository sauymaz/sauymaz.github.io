# Manual academic data import

This folder supports a manual, reviewable workflow for maintaining the static website. It does not scrape or fetch YOK Akademik data at runtime.

## Prepare CSV data

1. Open the relevant record list in YOK Akademik, Excel, or another trusted source.
2. Copy the information into the matching CSV template in this folder.
3. Keep the header row unchanged. Save the file as UTF-8 CSV.
4. Separate multiple `keywords` or `outputs` values with semicolons, for example: `machine learning; optimization; medical imaging`.
5. Use `true`, `false`, `yes`, `no`, `1`, or `0` for `featured` values.
6. Review author names, years, DOI values, URLs, and sources before importing.

The expected `publications.csv` columns are:

```text
id,year,category,publicationType,title,authors,venue,publisher,editors,volume,issue,pages,doi,url,isbn,presentationType,keywords,featured,source
```

Publication records are grouped on the site only as Articles, Conference Papers, and Books & Book Chapters. No international/national scope is stored or displayed; an extra legacy `scope` column, if present in an older CSV, is ignored by the importer.

## Import CSV data

Run these commands from the repository root with Python 3:

```bash
python scripts/import-publications-from-csv.py
python scripts/import-projects-from-csv.py
python scripts/import-academic-experience-from-csv.py
```

Each command writes formatted UTF-8 JSON to `src/data/` and prints its imported record count. Optional `--input` and `--output` arguments allow a different source or target path.

## Build and deploy

After checking the generated JSON, run:

```bash
npm run build
```

Commit the updated CSV and JSON files. A push to `main` triggers the GitHub Pages workflow, which builds and deploys the static site.
