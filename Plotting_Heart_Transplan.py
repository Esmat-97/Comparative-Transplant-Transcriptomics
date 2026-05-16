import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# اقرأ البيانات
data = pd.read_csv("GSE4315_series_matrix.txt",
                   sep="\t",
                   comment="!",
                   index_col=0)




# اقرأ الـ annotation
anno = pd.read_csv("GPL96-57554.txt", sep="\t", comment="#", skiprows=range(0, 16))
anno = anno[["ID", "Gene Symbol"]].dropna()

# اربط البيانات بالـ annotation
data_with_genes = data.merge(anno, left_index=True, right_on="ID")
data_with_genes = data_with_genes.set_index("Gene Symbol")






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
