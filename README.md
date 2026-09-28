# ChIP-seq analysis: Python and SQL practice
Python (pandas) and SQL (SQLite) scripts for exploring a public H3K9ac ChIP-seq differential peak table.

- load_chipseq.py: loads the table and filters peaks
- merge_genes.py: merges peaks with a gene list using pandas
- sql_practice.py: loads the table into SQLite and runs SELECT, WHERE, GROUP BY and ORDER BY queries

Data: GEO accession GSE249959 (not included in this repo).

Status: in progress. Next: reproducing ortholog mapping with pybiomart.
## Requirements
- Python 3
- pandas (`pip install pandas`)

## How to run
1. Download the differential peak table from GEO accession GSE249959.
2. Save it in this folder as `Chip_seq data.txt` (tab-separated).
3. For merge_genes.py, add `gene_name_map.csv` with a `Query` column of uppercase gene symbols.
4. Run any script, e.g. `python load_chipseq.py`

## Data
GEO accession GSE249959 (not included in this repo).

## Status
In progress. Next: reproducing ortholog mapping with pybiomart.
