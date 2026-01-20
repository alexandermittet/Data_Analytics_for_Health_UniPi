# Data Analytics for Digital Health - Analysis of Hospitalized Patients

**University of Pisa** - Department of Computer Science  
**Course:** Data Analytics for Digital Health  
**Academic Year:** 2025/2026

**Authors:** Alexander Mittet, Dominik Garstenauer  
**Supervisors:** Prof. Anna Monreale, Prof. Francesca Naretto

---

## Project Overview

This project performs comprehensive data mining and machine learning analysis on a cardiovascular patient cohort. The work covers the full data science pipeline: from data understanding and preprocessing, through unsupervised clustering, to supervised classification—applied to both tabular clinical data and ECG time series signals.

## Dataset

The analysis is based on four medical datasets comprising **4,864 hospitalized cardiac patients**:

- **Heart Diagnoses** (4,864 × 25) - Patient demographics, ICD codes, clinical notes
- **Laboratory Events** (978,503 × 14) - Lab test results (glucose, potassium, creatinine, etc.)
- **Microbiology Events** (15,587 × 14) - Culture results, antibiotic sensitivity
- **Procedure Codes** (14,497 × 6) - Cardiovascular interventions (angiography, angioplasty)

## Methods and Results

### 1. Data Understanding and Preparation

- Cleaned non-standard missing values and standardized data types across all datasets
- Merged datasets into unified patient profiles using (`subject_id`, `hadm_id`) keys
- Engineered 11 composite clinical features including:
  - Metabolic Stress Index, Renal Injury Score, Oxygenation Dysfunction Index
  - Inflammation/Liver Stress Index, Hematologic Stability Score
  - Micro Resistance Score, Procedure Density

### 2. Clustering Analysis (Tabular Data)

Applied three clustering algorithms to identify patient phenotypes:

- **K-means** (k=2): Silhouette 0.635, identified high-severity vs. baseline patients
- **DBSCAN** (eps=6.14): Silhouette 0.868, best separation with outlier detection
- **Hierarchical** (Ward, k=3): Silhouette 0.64, granular severity spectrum

**Result:** DBSCAN achieved the best cluster quality, identifying clinically distinct patient subgroups.

### 3. Classification Analysis (Tabular Data)

Binary classification of ischemic vs. non-ischemic cardiovascular conditions:

- **Best Model:** Gradient Boosting (ROC-AUC = 0.930, Balanced Accuracy = 0.860)
- **Key Predictors:** `has_hf` (heart failure), `total_procedures`, `has_valvular`
- Other models evaluated: Logistic Regression, KNN, SVM, Decision Tree, Random Forest

### 4. Time Series Preprocessing

Processed **1,786 ECG Lead II recordings** (5,000 samples each at 500 Hz):

- Applied bandpass filtering (0.5–40 Hz) and notch filtering (60 Hz)
- Z-normalization and linear trend removal
- Piecewise Aggregate Approximation (PAA) for dimensionality reduction

### 5. Time Series Clustering

Clustered ECG signals using PAA features:

- **K-means** (k=5): Silhouette 0.210
- **Hierarchical** (Ward): Silhouette 0.231
- **DBSCAN**: 27 clusters + 168 noise points

**Finding:** Lower silhouette scores compared to tabular clustering indicate ECG patterns represent continuous physiological processes rather than discrete clinical phenotypes.

### 6. Time Series Classification

Binary ischemic/non-ischemic classification on ECG data (1,184 patients):

- Features: PAA (30), SAX (30), DFT (30), HRV (6) = 96 total features
- **Best Model:** Shapelet classifier (F1 = 0.576, Recall = 0.661)
- Modest performance suggests global approximation features may not capture subtle ST-segment and T-wave changes indicative of ischemia

---

## Key Visualizations

### Piecewise Aggregate Approximation (PAA)

PAA compresses each 5,000-sample ECG signal into representative segments while preserving overall morphology for efficient clustering.

![PAA Approximation](tex/plots/3.1_paa_approximation.jpg)

### Classification: Tree-Based Feature Importance

`has_hf` (heart failure) emerges as the dominant predictor across Decision Tree, Random Forest, and Gradient Boosting models.

![Tree Feature Importance](tex/plots/4_classification_30_0.png)

### Time Series Clustering: KMeans Cluster Profiles

KMeans clustering on PAA features reveals distinct ECG temporal patterns across 5 clusters.

![KMeans Cluster Profiles](tex/plots/5.2_kmeans_cluster_profiles.jpg)

### Time Series Classification: Model Comparison

Comparison of classification performance metrics across all models. Shapelet, SVM, and ensemble methods outperform the linear baseline.

![TS Classification Metrics](tex/plots/6.tsc_metrics_comparison.jpg)

### Shapelet Feature Importance

The Shapelet classifier achieves the best F1-score by capturing local discriminative patterns in the ECG signals.

![Shapelet Feature Importance](tex/plots/6.tsc_shapelet_feature_importances.jpg)

### Top Shapelets Visualization

Visualization of the most discriminative shapelets, likely corresponding to QRS complexes and ST segments altered in ischemic conditions.

![Top Shapelets](tex/plots/6.tsc_top_shapelets_visualization.jpg)

---

## Repository Structure

```
├── code/                    # Jupyter notebooks for analysis
├── Data/                    # Processed CSV files and patient profiles
├── plots/                   # Generated visualizations
├── submission/              # Final submission notebooks
├── tex/                     # LaTeX report source files
│   ├── main.tex
│   ├── plots/               # Report figures
│   └── chapters/            # Individual chapter .tex files
└── requirements.txt         # Python dependencies
```

## Key Findings

1. **Tabular clustering** successfully identifies clinically meaningful patient phenotypes based on multi-organ dysfunction indices
2. **Tabular classification** achieves strong predictive performance (AUC > 0.93) for ischemic heart disease
3. **ECG time series** exhibit continuous variation rather than discrete clusters, suggesting PAA-based features capture general cardiac activity rather than specific disease states
4. **Shapelet-based methods** show promise for ECG classification by capturing local discriminative patterns

## Technologies

- Python 3.x
- pandas, numpy, scipy
- scikit-learn, XGBoost
- matplotlib, seaborn
- LaTeX (report)
