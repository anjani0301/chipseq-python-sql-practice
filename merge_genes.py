import pandas as pd

df_chip = pd.read_csv("Chip_seq data.txt", sep="\t")
df_map = pd.read_csv("gene_name_map.csv")

print(df_chip.shape)
print(df_map.shape)
print(df_map.columns.tolist())
print(df_map.head())
df_chip["Gene.Name.upper"] = df_chip["Gene.Name"].str.upper()

merged = pd.merge(df_chip, df_map, left_on="Gene.Name.upper", right_on="Query", how="inner")

print(merged.shape)
print(merged.columns.tolist())
print(merged[["Gene.Name", "Query", "Status", "logFC"]])
print(merged["Gene.Name"].value_counts())
peak_counts = df_chip.groupby("Status").size()
print(peak_counts)
