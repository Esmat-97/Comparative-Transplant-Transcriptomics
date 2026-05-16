🧬 Comparative Transplant Transcriptomics
📌 Overview

This project provides a comparative transcriptomic framework to study immune responses across different transplant settings, with a focus on rejection versus tolerance mechanisms.

By integrating publicly available GEO transcriptomic datasets from heart and corneal transplantation, the workflow identifies and visualizes immune pathway dynamics associated with inflammatory activation, immune regulation, and graft tolerance.

The pipeline combines:

GEO dataset processing
Probe-to-gene annotation
Immune signature scoring
Correlation analysis
Temporal trajectory visualization

The project is designed as a reproducible foundation for transplant immunology, systems immunology, and precision medicine research.

🧬 Datasets
Transplant Type	GEO Accession
Heart Transplant	GSE4315
Corneal Transplant	GSE232177
Annotation Platforms
GPL96-57554
GPL24324-69524

All datasets were obtained from the NCBI GEO repository.

⚙️ Workflow
1️⃣ Data Import & Annotation
Load GEO Series Matrix files
Parse expression matrices
Map probe IDs to gene symbols using GEO platform annotations
Clean and harmonize datasets across platforms
2️⃣ Immune Signature Scoring

Immune-related pathways are quantified using predefined gene signatures.

Included Signatures
Inflammation
Chemokine signaling
T-cell exhaustion
Treg / immune tolerance
NFκB signaling
NFAT signaling
IFNG axis

For each sample:

genes belonging to a signature are extracted
average normalized expression is calculated
pathway activity scores are generated
3️⃣ Visualization
🔥 Immune Signature Heatmaps

Visualize pathway activity across transplant conditions and samples.

🔗 Correlation Analysis

Evaluate relationships between immune programs, including:

Chemokine ↔ IFNG axis
Treg ↔ inflammatory pathways
Exhaustion ↔ tolerance markers
📈 Temporal Gene Trajectories

Track dynamic changes in key immune genes across transplant stages:

Before transplant
During rejection
Post-transplant / tolerance phase

Representative genes include:

IFNG
TNF
FOXP3
PDCD1
CXCL9
CXCL10
🔬 Comparative Transplant Analysis

The framework enables direct comparison between:

highly inflammatory solid-organ transplantation (heart)
relatively immune-privileged transplantation (cornea)

This allows identification of:

rejection-associated immune activation
tolerance-associated regulatory programs
preserved versus divergent immune pathways

Particular emphasis is placed on:

IFNG-driven inflammatory signaling
chemokine recruitment programs
maintenance of FOXP3-associated tolerance signatures
exhaustion-related immune modulation
📊 Example Outputs
Output	Description
immune_signatures.png	Heatmap of immune pathway activity
correlation_analysis.png	Correlation matrix between immune signatures
gene_timecourse.png	Temporal trajectories of key immune genes
🛠️ Requirements
Python
Python ≥ 3.9
Required Libraries
pip install pandas numpy seaborn matplotlib scikit-learn networkx
🚀 Usage

Run the main analysis script:

python immune_signature_analysis.py

Generated outputs:

immune_signatures.png
correlation_analysis.png
gene_timecourse.png
🎯 Project Goals

This repository aims to:

Provide a reproducible workflow for comparative transplant transcriptomics
Characterize immune rejection versus tolerance programs
Visualize immune pathway dynamics across transplant contexts
Support translational and precision immunology research
Serve as a scalable foundation for future multi-omics integration
📚 Future Directions

Potential extensions include:

Single-cell transcriptomic integration
Spatial transcriptomics
Machine learning–based immune state classification
Cell–cell communication analysis
Cross-organ transplant immune atlases
👨‍🔬 Research Context

This project was developed as part of ongoing interests in:

transplant immunology
immune tolerance biology
Treg stability and FOXP3 maintenance
inflammatory signaling networks
translational computational immunology
