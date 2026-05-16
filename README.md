Comparative Transplant Transcriptomics
📌 Project Overview
This repository provides a comparative transcriptomic analysis of immune signatures in different transplant contexts (e.g., heart vs. corneal transplants).
The workflow integrates GEO RNA-seq datasets with gene annotation, computes immune pathway scores, and visualizes rejection vs tolerance mechanisms through heatmaps, correlation plots, and gene trajectories.

🧬 Data Sources
Heart transplant dataset: GSE4315

Corneal transplant dataset: GSE232177

Annotation files: GPL96-57554, GPL24324-69524

Data retrieved from NCBI GEO (Gene Expression Omnibus).

⚙️ Workflow
Data Import & Annotation

Read GEO series matrix files.

Map probe IDs → gene symbols using platform annotation.

Immune Signature Scoring

Predefined gene sets for pathways:

Inflammation, Chemokine, T-cell exhaustion, Treg, NFkB, NFAT, IFNG axis.

Compute average expression per signature across samples.

Visualization

Heatmaps of immune signatures across samples.

Correlation analysis between pathways (e.g., Chemokine vs IFNG).

Gene expression trajectories across timepoints (Before, During, After transplant).

Comparative Analysis

Contrast immune landscapes between corneal and heart transplants.

Highlight differences in rejection vs tolerance mechanisms.

📊 Example Outputs
Immune Signature Heatmap → pathway activity across samples.

Correlation Heatmap → relationships between immune axes.

Trajectory Plots → dynamics of key genes (IFNG, TNF, FOXP3, PDCD1, CXCL9, CXCL10).

🛠️ Requirements
Python ≥ 3.9

Libraries:

bash
pip install pandas numpy seaborn matplotlib scikit-learn networkx
🚀 Usage
Run the analysis script:

bash
python immune_signature_analysis.py
Outputs:

immune_signatures.png

correlation_analysis.png

gene_timecourse.png

🎯 Goal
This repository aims to:

Provide a reproducible workflow for immune transcriptomic comparison in transplant biology.

Enable visualization of immune tolerance vs rejection signatures.

Serve as a foundation for precision immunology and translational research.
