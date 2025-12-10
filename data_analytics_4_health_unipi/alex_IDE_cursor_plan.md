# Health Data Analytics Project - Progress Update

## Completed Tasks

### ✅ Task 1.1.2: Merge Datasets

**Status:** COMPLETED

- Created `code/1.1.2 merge_datasets.ipynb` with both merge strategies
- **Option A:** Merge on `subject_id` only (patient-level) → `1.1.2_merged_dataset_option_a_subject_id.csv`
- **Option B:** Merge on `(subject_id, hadm_id)` pair (admission-level) → `1.1.2_merged_dataset_option_b_subject_hadm_id.csv`
- Implemented data cleaning: removes hadm_ids with multiple subject_ids
- Fixed file naming to use task prefixes (1.1.2_)
- Fixed ID columns to save as integers (not floats)
- Generated merged datasets with proper aggregation (mean, count for numeric columns)

### ✅ Task 1.2.2: Feature Engineering - Time Features

**Status:** COMPLETED

- Created `code/1.2 feature_engineering_time_features.ipynb`
- Implemented features:
  - `n_total_admissions`: Total number of unique admissions per subject_id
  - `days_since_last_admission`: Mean days between consecutive admissions per subject_id
- Saved outputs: `1.2_subject_time_features.csv`, `1.2_admission_time_features.csv`

### ✅ Task 1.1: Data Understanding (Partial)

**Status:** MOSTLY COMPLETED

- EDA completed in `code/1.1 task.ipynb`
- Distributions, correlations, boxplots generated
- Plots saved in `plots/` directory
- **Remaining:** NaN handling decisions, "none \n\n" conversion to NaN

## In Progress / Next Steps

### 🔄 Task 1.2.2: Feature Engineering - Additional Features

**Status:** PARTIALLY COMPLETED

- ✅ Time-based features (n_total_admissions, days_since_last_admission)
- ✅ Laboratory features (n_lab_events, abnormal_ratio, max_glucose) - from 1.1 task.ipynb
- ✅ Microbiology feature (n_micro_exam) - from 1.1 task.ipynb
- ✅ Procedure feature (total_procedures) - from 1.1 task.ipynb
- **TODO:** Think of more features (one for each df at least) to reach ~10 total features

### ⏳ Task 1.2.1: Transformations, NaN Removal, Outlier Handling

**Status:** NOT STARTED

- z normalization per column
- Outlier removal decisions
- Remove qc_flag == FAIL (partially done in 1.1 task.ipynb for df2)

### ⏳ Task 2: Clustering Analysis

**Status:** NOT STARTED

- K-means clustering
- Density-based clustering
- Hierarchical clustering

### ⏳ Task 3: Time Series Analysis

**Status:** NOT STARTED

- Create time series per subject_id
- Pre-process time series
- Extract features or approximate

## Current Feature Count

- Laboratory: n_lab_events, abnormal_ratio, max_glucose (3 features)
- Microbiology: n_micro_exam (1 feature)
- Procedures: total_procedures (1 feature)
- Time-based: n_total_admissions, days_since_last_admission (2 features)
- **Total: ~7 features** (Goal: ~10 features)

## Files Created/Modified

- `code/1.1.2 merge_datasets.ipynb` - Merge strategies implementation
- `code/1.2 feature_engineering_time_features.ipynb` - Time-based features
- `Data/1.1.2_merged_dataset_option_a_subject_id.csv` - Patient-level merged data
- `Data/1.1.2_merged_dataset_option_b_subject_hadm_id.csv` - Admission-level merged data
- `Data/1.2_subject_time_features.csv` - Subject-level time features
- `Data/1.2_admission_time_features.csv` - Admission-level time features

## Notes

- All CSV files use task number prefixes (1.1.2_, 1.2_) for organization
- ID columns (subject_id, hadm_id) are saved as integers
- Backup files created before regenerating merged datasets
