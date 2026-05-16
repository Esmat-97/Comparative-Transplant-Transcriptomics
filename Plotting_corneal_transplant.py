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





import seaborn as sns
import numpy as np

data = np.random.rand(10, 5)  # 10 samples × 5 immune markers
sns.heatmap(data, cmap="viridis")
plt.title("Immune Signature Heatmap")
plt.show()





time = np.arange(0,10,1)
chemokine = np.sin(time) + np.random.rand(len(time))*0.2

plt.plot(time, chemokine, marker='o')
plt.title("Chemokine Trajectory")
plt.xlabel("Time")
plt.ylabel("Chemokine Level")
plt.show()







pathway_scores = np.random.rand(20)
plt.bar(range(len(pathway_scores)), pathway_scores)
plt.title("Pathway Score (PD-1 axis)")
plt.xlabel("Samples")
plt.ylabel("Score")
plt.show()






import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ("PD-1", "Immune suppression"),
    ("Chemokine", "Cell migration"),
    ("Pathway", "Response outcome")
])

nx.draw(G, with_labels=True, node_color="lightblue", node_size=2000, font_size=10)
plt.title("Mechanism Model Diagram")
plt.show()
