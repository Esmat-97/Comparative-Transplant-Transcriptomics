# 🧬 Comparative Transplant Transcriptomics

---

# 📌 Overview

This project provides a comparative transcriptomic framework to study immune responses across different transplant settings, with a focus on **rejection versus tolerance mechanisms**.

By integrating publicly available GEO transcriptomic datasets from **heart** and **corneal transplantation**, the workflow identifies and visualizes immune pathway dynamics associated with inflammatory activation, immune regulation, and graft tolerance.

The pipeline combines:

- GEO dataset processing  
- Probe-to-gene annotation  
- Immune signature scoring  
- Correlation analysis  
- Temporal trajectory visualization  

This repository is designed as a reproducible foundation for:

- **Transplant Immunology**
- **Systems Immunology**
- **Precision Medicine Research**

---

# 🧬 Datasets

| Transplant Type | GEO Accession |
|-----------------|---------------|
| Heart Transplant | `GSE4315` |
| Corneal Transplant | `GSE232177` |

## Annotation Platforms

- `GPL96-57554`
- `GPL24324-69524`

All datasets were obtained from the **NCBI GEO repository**.

---

# ⚙️ Workflow

---

## 1️⃣ Data Import & Annotation

- Load GEO Series Matrix files  
- Parse expression matrices  
- Map probe IDs to gene symbols using GEO platform annotations  
- Harmonize datasets across platforms  

---

## 2️⃣ Immune Signature Scoring

Immune-related pathways are quantified using predefined gene signatures.

### Included Signatures

- Inflammation  
- Chemokine signaling  
- T-cell exhaustion  
- Treg / immune tolerance  
- NFκB signaling  
- NFAT signaling  
- IFNG axis  

### Scoring Strategy

For each sample:

- Extract genes belonging to a signature  
- Compute average normalized expression  
- Generate pathway activity scores  

---

## 3️⃣ Visualization

### 🔥 Immune Signature Heatmaps

Visualize pathway activity across transplant conditions and samples.

---

### 🔗 Correlation Analysis

Evaluate relationships between immune programs, including:

- Chemokine ↔ IFNG axis  
- Treg ↔ inflammatory pathways  
- Exhaustion ↔ tolerance markers  

---

### 📈 Temporal Gene Trajectories

Track dynamic changes in key immune genes across transplant stages:

- Before transplant  
- During rejection  
- Post-transplant / tolerance phase  

### Representative Genes

- `IFNG`
- `TNF`
- `FOXP3`
- `PDCD1`
- `CXCL9`
- `CXCL10`

---

# 🔬 Comparative Analysis

This framework enables direct comparison between:

- Highly inflammatory solid-organ transplantation (**heart**)  
- Immune-privileged transplantation (**cornea**)  

The analysis highlights:

- Rejection-associated immune activation  
- Tolerance-associated regulatory programs  
- Preserved versus divergent immune pathways  

Special emphasis is placed on:

- IFNG-driven inflammatory signaling  
- Chemokine recruitment programs  
- Maintenance of `FOXP3`-associated tolerance  
- Exhaustion-related immune modulation  

---

# 📊 Example Outputs

| Output File | Description |
|-------------|-------------|
| `immune_signatures.png` | Immune pathway activity heatmap |
| `correlation_analysis.png` | Correlation matrix between immune signatures |
| `gene_timecourse.png` | Temporal trajectories of immune genes |

---

# 🛠️ Requirements

## Python Version

- Python ≥ 3.9

---

Inflammatory signaling networks
Translational computational immunolog
