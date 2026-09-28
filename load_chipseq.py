import pandas as pd
df = pd.read_csv("Chip_seq data.txt", sep="\t")
print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df.tail())
down_genes = df[(df["Status"] == "Down") & (df["FDR"] < 0.05)]
print(down_genes.shape)
print(down_genes[["Gene.Name", "logFC", "FDR"]].head(10))

