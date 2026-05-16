import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1️⃣ اقرأ البيانات (series matrix + annotation)
data = pd.read_csv("GSE232177_series_matrix.txt", sep="\t", comment="!", index_col=0)


# قراءة ملف الانوتيشن
anno = pd.read_csv(
    "GPL24324-69524.txt",
    sep="\t",
    comment="#",
    low_memory=False
)


# print(data.index[:5])
# print(anno["ID"].head())

# # عرض أول IDs
# print(anno["ID"].head())

anno = anno[["ID", "SPOT_ID.1"]].copy()

anno["Gene"] = anno["SPOT_ID.1"].str.extract(
    r'Homo sapiens .*? \(([A-Z0-9\-]+)\)'
)


anno = anno.dropna(subset=["Gene"])

anno = anno[["ID", "Gene"]]



data_with_genes = data.merge(
    anno,
    left_index=True,
    right_on="ID",
    how="inner"
)

data_with_genes = data_with_genes.set_index("Gene")

data_with_genes = data_with_genes.drop(columns=["ID"])

# print(data_with_genes.index)

# gene_names = data_with_genes.index.tolist()
# print(len(gene_names))   # عدد الجينات

# print(data_with_genes.index[:20])







# 2️⃣ عرف الـ signatures
signatures = {
    "Inflammation": ["TNF", "IFNG", "IL1B", "IL6"],
    "Chemokine": ["CXCL9", "CXCL10", "CCL5"],
    "Tcell_exhaustion": ["PDCD1", "CTLA4", "LAG3", "TIGIT", "HAVCR2"],
    "Treg": ["FOXP3", "IL2RA", "IKZF2"],
    "NFkB": ["NFKB1", "RELA", "TNFAIP3", "ICAM1"],
    "NFAT": ["NFATC1", "IL2", "EGR2"],
    "IFNG_axis": ["IFNG","STAT1","IRF1","CXCL11"],
    "NeuroGenes": ["Nrn1", "Atp2b2", "Ddit4"] ,
    "DC_signature": ["Clec9a", "Xcr1", "Tsc22d3"]
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
sns.heatmap(scores_df.T, cmap="coolwarm")
plt.title("Immune Signatures - - GSE232177 (corneal_transplant")
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
plt.title("Correlation Analysis - GSE232177 (corneal_transplant)")
plt.show()












import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# اقرأ الـ metadata كله
metadata = {}
with open("GSE232177_series_matrix.txt", "r") as f:
    for line in f:
        if line.startswith("!Sample_characteristics_ch1"):
            # خزن كل الـ characteristics
            if "characteristics" not in metadata:
                metadata["characteristics"] = []
            metadata["characteristics"].append(line.strip().split("\t")[1:])

# حول الـ characteristics لمصفوفة (كل عمود = نوع characteristic)
metadata_df = pd.DataFrame(metadata["characteristics"]).T
# print("Metadata columns:")
# print(metadata_df.head())

# دور على العمود اللي فيه كلمة time
time_col = None
for col in metadata_df.columns:
    if metadata_df[col].str.contains("time", case=False, na=False).any():
        time_col = col
        break

# print("Time column index:", time_col)

# اعمل mapping للوقت
time_points = []
for char in metadata_df[time_col]:
    char = char.lower()
    if "before" in char:
        time_points.append(0)
    elif "6" in char and "month" in char:
        time_points.append(180)
    elif "12" in char and "month" in char:
        time_points.append(365)
    else:
        time_points.append(np.nan)

# أهم 6 جينات مناعية
top_genes = ["IFNG", "TNF", "CXCL9", "CXCL10", "FOXP3", "PDCD1"]
sample_cols = data.columns

# نبني DataFrame طويل (long format) باستخدام time_points اللي استخرجناه
plot_data = []
for gene in top_genes:
    expr_values = data_with_genes.loc[gene, sample_cols].values.flatten()
    for t, val in zip(time_points, expr_values):
        plot_data.append({
            "time_days": t,
            "gene": gene,
            "expression": float(val)
        })

plot_df = pd.DataFrame(plot_data)

# print(plot_df)






import seaborn as sns
import matplotlib.pyplot as plt

# Pivot: نخلي الجدول على شكل (time_days × gene)
heatmap_df = plot_df.pivot_table(
    index="time_days",   # المحور الرأسي = الوقت
    columns="gene",      # الأعمدة = الجينات
    values="expression", # القيم = التعبير الجيني
    aggfunc="mean"       # ناخد المتوسط لو فيه عينات متعددة في نفس الوقت
)

print(heatmap_df)

# نرسم Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_df, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Heatmap of Top 6 Immune Genes (Corneal Transplant)")
plt.xlabel("Gene")
plt.ylabel("Days after transplant")
plt.show()








