# ChIP-seq analysis: Python and SQL practice
Python (pandas) and SQL (SQLite) scripts for exploring a public H3K9ac ChIP-seq differential peak table.

- load_chipseq.py: loads the table and filters peaks
- merge_genes.py: merges peaks with a gene list using pandas
- sql_practice.py: loads the table into SQLite and runs SELECT, WHERE, GROUP BY and ORDER BY queries

Data: GEO accession GSE249959 (not included in this repo).
Status: in progress. Next: reproducing ortholog mapping with pybiomart.
