import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1️⃣ اقرأ البيانات (series matrix + annotation)
data = pd.read_csv("GSE4315_series_matrix.txt", sep="\t", comment="!", index_col=0)
# اقرأ الـ metadata
metadata = {}
with open("GSE4315_series_matrix.txt", "r") as f:
    for line in f:
        if line.startswith("!Sample_title"):
            metadata["title"] = line.strip().split("\t")[1:]
        if line.startswith("!Sample_characteristics_ch1"):
            metadata["characteristics"] = line.strip().split("\t")[1:]
        if line.startswith("!Sample_source_name_ch1"):
            metadata["source"] = line.strip().split("\t")[1:]

samples_df = pd.DataFrame(metadata, index=data.columns)








anno = pd.read_csv("GPL96-57554.txt", sep="\t", comment="#", skiprows=range(0,16))
anno = anno[["ID", "Gene Symbol"]].dropna()

# اربط الجينات بالـ expression
data_with_genes = data.merge(anno, left_index=True, right_on="ID")
data_with_genes = data_with_genes.set_index("Gene Symbol")




# 2️⃣ عرف الـ signatures
signatures = {
    "Inflammation": ["TNF", "IFNG", "IL1B", "IL6"],
    "Chemokine": ["CXCL9", "CXCL10", "CCL5"],
    "Tcell_exhaustion": ["PDCD1", "CTLA4", "LAG3", "TIGIT", "HAVCR2"],
    "Treg": ["FOXP3", "IL2RA", "IKZF2"],
    "NFkB": ["NFKB1", "RELA", "TNFAIP3", "ICAM1"],
    "NFAT": ["NFATC1", "IL2", "EGR2"],
    "IFNG_axis": ["IFNG","STAT1","IRF1","CXCL11"],
}

# 3️⃣ احسب الـ scores لكل عينة
sample_cols = data.columns
scores = {}
for sig, genes in signatures.items():
    present_genes = data_with_genes.index.intersection(genes)
    if len(present_genes) > 0:
        sig_values = data_with_genes.loc[present_genes, sample_cols].mean()
        scores[sig] = sig_values

scores_df = pd.DataFrame(scores)
print(scores_df)

# 4️⃣ Heatmap للـ signatures عبر العينات
sns.heatmap(scores_df.T, cmap="coolwarm", annot=True)
plt.title("Immune Signatures - GSE4315 (Heart Transplant)")
plt.show()









correlations = {
    "Chemokine_vs_IFNG": scores_df["Chemokine"].corr(scores_df["IFNG_axis"]),
    "Treg_vs_IFNG": scores_df["Treg"].corr(scores_df["IFNG_axis"]),
    "NFkB_vs_Exhaustion": scores_df["NFkB"].corr(scores_df["Tcell_exhaustion"]),
}

# تحويل لجدول مرتب
corr_df = pd.DataFrame.from_dict(correlations, orient="index", columns=["Correlation"])
print(corr_df)

# رسم Heatmap للارتباطات
sns.heatmap(corr_df, cmap="coolwarm", annot=True, vmin=-1, vmax=1)
plt.title("Correlation Analysis - GSE4315 (Heart Transplant)")
plt.show()






import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Array للـ timepoints (مثال: 9 عينات)
time_array = np.array([
    "Before","Before","Before",
    "During","During","During",
    "After","After","After"
])

# أهم 6 جينات مناعية
top_genes = ["IFNG", "TNF", "CXCL9", "CXCL10", "FOXP3", "PDCD1"]

# نبني DataFrame طويل (long format)
plot_data = []
for gene in top_genes:
    expr_values = data_with_genes.loc[gene, sample_cols].values.flatten()  # تأكد إنها 1D
    for t, val in zip(time_array, expr_values):
        plot_data.append({
            "timepoint": t,
            "gene": gene,
            "expression": float(val)  # نحول القيمة لرقم صريح
        })

plot_df = pd.DataFrame(plot_data)




import seaborn as sns
import matplotlib.pyplot as plt

# Pivot: نخلي الجدول على شكل (timepoint × gene)
heatmap_df = plot_df.pivot_table(
    index="timepoint",   # المحور الرأسي = الوقت
    columns="gene",      # الأعمدة = الجينات
    values="expression", # القيم = التعبير الجيني
    aggfunc="mean"       # ناخد المتوسط لو فيه عينات متعددة في نفس الوقت
)

print(heatmap_df)

# نرسم Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_df, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Heatmap of Top 6 Immune Genes (Heart Transplant)")
plt.xlabel("Gene")
plt.ylabel("Timepoint")
plt.show()

