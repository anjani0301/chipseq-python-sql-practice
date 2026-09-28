import sqlite3
import pandas as pd

df = pd.read_csv("Chip_seq data.txt", sep="\t")
conn = sqlite3.connect("chipseq.db")
df.to_sql("peaks", conn, if_exists="replace", index=False)

result = pd.read_sql("SELECT COUNT(*) FROM peaks", conn)
print(result)
down_peaks = pd.read_sql("SELECT * FROM peaks WHERE Status = 'Down' AND FDR < 0.05", conn)
print(down_peaks.shape)
print(down_peaks[["Gene.Name", "logFC", "FDR"]])
status_counts = pd.read_sql("SELECT Status, COUNT(*) FROM peaks GROUP BY Status", conn)
print(status_counts)
sorted_down = pd.read_sql("SELECT \"Gene.Name\", logFC, FDR FROM peaks WHERE Status = 'Down' ORDER BY FDR ASC", conn)
print(sorted_down)
