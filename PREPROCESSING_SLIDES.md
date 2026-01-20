# Data Preprocessing: The Story
## From Raw Clinical Data to Analysis-Ready Features

---

# Slide 1: The Challenge

## What We Started With

| Dataset | Rows | Key Issues |
|---------|------|------------|
| Heart Diagnoses | 4,864 | 72% missing gender/age, disguised NaNs |
| Laboratory | 978,503 | Placeholder values, mixed units, QC failures |
| Microbiology | 15,587 | Hierarchical missingness, negative cultures |
| Procedures | 14,497 | Clean! (our lucky dataset) |

**Goal**: Transform messy clinical data into meaningful features for analysis

---

# Slide 2: Our Philosophy

## Data Recovery Over Deletion

> "Every missing value tells a story. Before deleting, ask: Can we recover it?"

### Key Principles:
1. Recover values from complex strings
2. Use clinical context for imputation
3. Filter by quality, not by convenience
4. Document every decision

---

# Slide 3: Heart Diagnoses - The Detective Work

## The Problem
- **72% of gender values missing**
- **72% of age values missing**
- Clinical notes contain the answers!

## The Insight
> Medical records use gendered language: "she presented with...", "Mr. ___ is a 67 year-old man..."

---

# Slide 4: Gender Imputation Strategy

## 4-Stage Text Mining Approach

| Stage | Method | Rows Filled |
|-------|--------|-------------|
| 1 | Keywords: "female", "male", "woman", "man" | 2,383 |
| 2 | Clinical terms: "pregnant", "prostate" | 60 |
| 3 | Pronouns: she/her vs he/his (majority vote) | 837 |
| 4 | Manual review of remaining cases | 4 |

### Result: 99.8% of missing gender recovered!

---

# Slide 5: Age Imputation Strategy

## Sequential Group Median Approach

```
Step 1: Group by (ICD Code + Gender)
        -> Use median if N >= 100 samples
        -> Filled 2,062 rows

Step 2: Group by (ICD Code only)
        -> Fallback for smaller groups
        -> Filled 795 rows
```

### Result: 81.6% of missing ages imputed

**Why N=100?** Balance between coverage and statistical reliability

---

# Slide 6: Heart Features Created

## From Text to Numbers

| Feature Type | Examples |
|--------------|----------|
| Mortality | `is_dead` from date of death |
| Imaging | `n_imaging_tests`, `imaging_variety` |
| Cardiac Phenotype | `has_hf`, `has_ami`, `has_arr` |
| Documentation | `doc_complexity_index` (log text length) |

### ICD Categories: acute_mi, heart_failure, arrhythmia, valvular...

---

# Slide 7: Laboratory Data - Value Recovery

## The Problem with Raw Values

```
value column examples:
  "___"        -> Placeholder (convert to NaN)
  "20/10"      -> Division (calculate: 2.0)
  "80-160"     -> Range (take midpoint: 120)
  ">1.05"      -> Comparison (offset: 1.15)
```

### Result: Recovered 1,311 additional numeric values

---

# Slide 8: Laboratory Quality Control

## Trust the QC Flags

| QC Status | Action | Rows Affected |
|-----------|--------|---------------|
| QC_FAIL | Set to NaN | 18,185 (1.86%) |
| QC_WARN | Keep but flag | 78,124 (8%) |
| QC_OK | Use as-is | 882,194 (90%) |

**Rationale**: Failed quality control = unreliable measurement

---

# Slide 9: Unit Normalization

## Making Apples Equal Apples

| Analyte | From | To | Factor |
|---------|------|-----|--------|
| Glucose | mg/dL | mmol/L | 0.0555 |
| Creatinine | mg/dL | umol/L | 88.4 |
| Hemoglobin | g/dL | g/L | 10.0 |
| pCO2 | mm Hg | kPa | 0.133 |

### 642,381 measurements standardized across 34 analytes

---

# Slide 10: Laboratory Features

## Aggregated Per Admission

**Activity Metrics**
- `num_labs`, `lab_time_span_hours`, `unique_lab_tests`

**Quality Indicators**
- `abnormal_ratio`, `qc_fail_ratio`

**Clinical Values by Fluid**
- Blood: glucose, lactate, creatinine, hemoglobin
- Urine: glucose, creatinine, sodium, protein
- Blood Gas: pO2, pCO2, pH, base excess

---

# Slide 11: Microbiology - Understanding Missingness

## Not All Missing Values Are Equal

```
+--------------------------------------------------+
| All three missing (org, ab, dilution): 10,195    |
|    +----------------------------------------+    |
|    | ab_name + dilution missing: 571        |    |
|    |    +------------------------------+    |    |
|    |    | dilution only: 362           |    |    |
|    |    +------------------------------+    |    |
|    +----------------------------------------+    |
|         Complete rows: 4,458                     |
+--------------------------------------------------+
```

**Key Insight**: Missing organism = NEGATIVE culture (clinically meaningful!)

---

# Slide 12: Microbiology Features

## Capturing Infection Patterns

| Category | Features |
|----------|----------|
| Diversity | `unique_organisms`, `unique_antibiotics` |
| Susceptibility | `num_resistant`, `resistant_ratio` |
| Activity | `total_microbio_events`, `micro_time_span_hours` |

### Antibiotic Interpretation:
- S = Susceptible (drug works)
- R = Resistant (drug fails)
- I = Intermediate (needs higher dose)

---

# Slide 13: Procedures - The Clean One

## Sometimes You Get Lucky!

- No duplicates
- No missing values
- Valid ICD codes (3-7 characters)

### Features Created:
- `total_procedures`
- `unique_icd_codes`
- `procedure_span_days`

**Observation**: r=0.98 correlation between count and unique codes
(Most procedures have unique codes)

---

# Slide 14: The Complete Pipeline

```
     Raw Data                    Cleaned Data              Features
+----------------+          +------------------+      +------------------+
| Heart (4.9K)   |--+       |                  |      |                  |
+----------------+  |       |   Remove Dupes   |      |  Heart: 18 vars  |
| Lab (978K)     |--+------>|   Handle NaNs    |----->|  Lab: 34 vars    |
+----------------+  |       |   QC Filtering   |      |  Micro: 17 vars  |
| Micro (15.5K)  |--+       |   Unit Normalize |      |  Proc: 6 vars    |
+----------------+  |       |   Parse Dates    |      |                  |
| Proc (14.5K)   |--+       +------------------+      +------------------+
+----------------+                                           |
                                                             v
                                                    ~75 Features Total
```

---

# Slide 15: Impact Summary

## What We Achieved

| Dataset | Before | After |
|---------|--------|-------|
| Heart Gender | 28% complete | 99.9% complete |
| Heart Age | 28% complete | 86% complete |
| Lab Values | 907K numeric | 908K numeric (+1,311) |
| Lab Quality | Unknown reliability | 90% QC-verified |

### Data Loss (Intentional):
- 18,185 QC-failed lab measurements (1.86%)
- 255 QC-failed microbiology results (1.64%)

---

# Slide 16: Key Decisions Recap

## Why These Choices Matter

| Decision | Rationale |
|----------|-----------|
| Text-based gender imputation | Preserves 99.8% vs deleting 72% |
| ICD+Gender age imputation | Clinically meaningful groupings |
| QC-based filtering | Quality > quantity |
| Unit standardization | Cross-patient comparability |
| Negative culture preservation | Clinically informative absence |

---

# Slide 17: Lessons Learned

## What This Project Taught Us

1. **Missing data has meaning** - negative cultures, unavailable tests
2. **Clinical text is rich** - pronouns, keywords reveal demographics
3. **Quality flags exist for a reason** - trust the lab QC
4. **Domain knowledge matters** - ICD codes group similar patients
5. **Document everything** - reproducibility requires transparency

---

# Slide 18: Final Output

## Ready for Analysis

| Dataset | Rows | Features | Aggregation Level |
|---------|------|----------|-------------------|
| Heart | 4,864 | 18 | Per admission |
| Laboratory | varies | 34 | Per admission |
| Microbiology | varies | 17 | Per admission |
| Procedures | varies | 6 | Per admission |

### All datasets linked by: (subject_id, hadm_id)

---

# Slide 19: Thank You

## Questions?

### Files Available:
- `heart_diagnoses_1_cleaned.csv` + `_agg_features.csv`
- `laboratory_events_codes_2_cleaned.csv` + `_agg_features.csv`
- `microbiology_events_codes_3_cleaned.csv` + `_agg_features.csv`
- `procedure_code_4_cleaned.csv` + `_agg_features.csv`

### Documentation:
- `PREPROCESSING_STORY.md` - Full methodology
- Jupyter notebooks - Step-by-step code

---

# Appendix: Feature Lists

## Heart Diagnoses (18 features)
`subject_id`, `hadm_id`, `gender`, `age`, `is_dead`, `charttime`, `icd_code`, `icd_cat`, `imaging_variety`, `doc_complexity_index`, `cardiac_comorbidity_score`, `has_heart`, `has_hf`, `has_arr`, `has_ami`, `has_arrest`, `has_valvular`, `has_inflammatory`

## Laboratory (34 features)
Activity, quality, blood values, urine values, blood gas, system counts...

## Microbiology (17 features)
Diversity, susceptibility, QC flags, temporal span...

## Procedures (6 features)
`total_procedures`, `unique_icd_codes`, `unique_titles`, `procedure_span_days`, `has_procedure`
