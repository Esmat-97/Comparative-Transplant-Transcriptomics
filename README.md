Comparative Transplant Transcriptomics
📌 Overview
This repository provides a comparative analysis of immune transcriptomic signatures in different transplant contexts (e.g., heart vs. corneal transplants).
The workflow integrates RNA-seq series matrix data with gene annotation, computes immune pathway scores, and visualizes results through heatmaps, correlation plots, and gene trajectories.

🧬 Data Sources
GEO datasets (e.g., GSE4315 for heart transplant, GSE232177 for corneal transplant).

Platform annotation files (e.g., GPL96-57554) to map probe IDs to gene symbols.

⚙️ Workflow
Data Import & Annotation

Read GEO series matrix files.

Merge with annotation to map probes → gene symbols.

Immune Signature Scoring

Predefined gene sets for pathways:

Inflammation, Chemokine, T-cell exhaustion, Treg, NFkB, NFAT, IFNG axis.

Compute average expression per signature across samples.

Visualization

Heatmaps of immune signatures across samples.

Correlation analysis between pathways (e.g., Chemokine vs IFNG).

Gene expression trajectories across timepoints (Before, During, After transplant).

Comparative Analysis

Compare immune landscapes between different transplant types.

Highlight differences in rejection vs tolerance mechanisms.

📊 Example Outputs
Immune Signature Heatmap: shows pathway activity across samples.

Correlation Heatmap: reveals relationships between immune axes.

Trajectory Plots: track gene expression (e.g., IFNG, TNF, FOXP3, PDCD1) over time.

🛠️ Requirements
Python 3.9+

Libraries: pandas, numpy, seaborn, matplotlib, scikit-learn, networkx

Install via:

bash
pip install pandas numpy seaborn matplotlib scikit-learn networkx
🚀 Usage
Run the analysis script:

bash
python immune_signature_analysis.py
Outputs will include:

Heatmaps (immune_signatures.png)

Correlation plots (correlation_analysis.png)

Gene trajectory heatmaps (gene_timecourse.png)

🎯 Goal
This repository aims to:

Provide a reproducible workflow for immune transcriptomic comparison in transplant biology.

Enable visualization of immune tolerance vs rejection signatures.

Serve as a foundation for precision immunology research.
