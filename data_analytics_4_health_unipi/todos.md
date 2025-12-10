//MAIN GOAL is to create a subject profile with about ~10 features in the end//

Task 1.1: data understanding
prof notes:
Explore the various dataset with the analytical tools studied and write a concise “data
understanding” report assessing data quality, the distribution of the variables and the
pairwise correlations.
There is a wide variety of data available and we strongly encourage you to link the
information across the different CSV files provided

My todo items:

- how to handle NaNs (age, gender of df1, ...) => remove / mean / ..
- "none \n\n" => convert to NaN
- check for more inconsistencies

1.1.2 Merge

- on which key? subejct id or subject & hadm ??
plan:
- Use a reference table (e.g., Diagnoses) with both hadm_id + subject_id.
- For datasets with only hadm_id, merge with reference to add subject_id.
- Compute all features per admission (hadm_id, subject_id).
- Merge datasets on both keys (hadm_id, subject_id) to keep integrity.
Finally, aggregate by subject_id to build patient-level profiles.

Todo items:
1.2.1 Transformations, NaN removal, otulier handling  

- z normalization per col
- outlier to remove?
- remove qc_flag == FAIL .. ?

1.2.2 Feature engineering - create one feature per dataset at least

- per subject_id: time since last admission
- per subject_id: total admission  
- DONE Total count of laboratory events linked to the admission
- DONE ratio between the number of tests flagged as abnormal and the total number
of tests?
- think of more features (one for each df at least)

2. clustering analysis
Based on the features extracted in the previous task, explore the dataset using the
clustering techniques presented during the lessons. You should explore the data after
the creation of your patient profile, hence after Data Understanding and Pre Processing.
Carefully describe your decisions for each algorithm and which are the advantages
provided by the different approaches.
Subtasks for tabular data

- Clustering Analysis by K-means on the entire dataset:
2.1.1 Identification of the best value of k
2.1.2 Characterization of the obtained clusters by using both analysis of
the k centroids and comparison of the distribution of variables within
the clusters and that in the whole dataset
2.1.3 Evaluation of the clustering results
- Analysis by density-based clustering:
2.2.1. Study of the clustering parameters
2.2.2 Characterization and interpretation of the obtained clusters
- Analysis by hierarchical clustering:
2.3.1 Compare different clustering results got by using different version of
the algorithm
2.3.2 Show and discuss different dendrograms using different algorithms
- Final evaluation of the best clustering approach and comparison of the clustering
obtained

3. time series
the time series data provided for this project is composed of ECG signals with 12 channels
for each record. We suggest building one time series for each patient: create one time series
for each subject_id and focus on simple, preferably univariate series (each series should
represent one specific type of information at a time). To achieve this, you should pre-process
the time series with the tools and approaches seen during the lessons. Then, you can decide
to approximate your time series or to extract features from it.
Note: the series can be short, and this is not a problem, just focus on the consistency of your
chosen subtask rather than the length of the sequence.

- Always start from the patient: create one time series for each subject_id containing
the timestamps and the corresponding values for the chosen event type.
- For diagnostic data, use the codes from the heart_diagnoses table, selecting those
associated with each subject_id. These codes, as well as all the other information
extracted from the tabular data, can enrich your analysis also from the time series
point of view

## ALEX notes 13. nov

Pca plots look interesting. Prob the professor did something to make the points look like that. 3 clear clusters but then a small tail/line down from the bottom area?

## Alex 14. nov

- 2.3 cluserting only has 2 clusters. I understand the method runs itself, however i dont believe k=2 says much about the data.
  - there is only 1 point iin cluster 1...

## NOTES FROM LECTURE 14.nov

- it's real data so there might be errors
- nothing prevents us from looking on web on what ranges to do etc
  - and put this source in the report
- remove as little as possible
- data comes from different hospitals, therefore there are duplicate hadms and subjs.
  - THE UNIQUE KEY IS THE PAIR!

# next steps

for laboratory_events_codes_2, turn these into one: (valuenum valueuom ref_range_lower ref_range_upper flag)
if ref is within range = 0
if above: +1
if its below the range: -1

- check for duplicated records

# DECISIONS WE MADE

- we removed the "value" column from laboratory_events_codes_2 since its just a bad version of the valuenum column
- we checked for numerics values
- we fixed mixed types like the .0 IDs
- we parsed the datetime column
- we remove DOD since it is not described in the PDF from professors
- remove one of charttime or storetime since they are similar
- remove qc_flag == FAIL
  - bad data in => bad data out
  - if we look at only QC fail, we should chack how many NaNs and outliers are in here. If its higher than QC okay, then this is our motivation



# Plan for 1.1 & 1.2 Dominik 21.11
PLAN Dominik:

Clean all datasets → add missing subject_id → compute admission-level features PER dataset → merge admission-level tables → aggregate to patient-level for clustering.

**Step 1:** Clean each DF
- 1. common core cleaning to all 4 dfs
- 2. dataset specific cleaning
errors: 
    - wrong dtypes: ensure numerical are correct (.0, whitespace, dtypes..), enforcing integer hadm_id and subject_id
    - convert dates to datetimes etc (dod needs to be handled seperatly)
    - standardize categorical columns to string (note_type, label, fluid, spec_type_desc, org_name, ab_name, interpretation, icd_code)
    - text fields: strip whitespace and convert empty strings to NaN.
    - Lab: ensure valuenum is numeric; extract numbers from value when possible
    - Microbiology: cast dilution_value to float; invalid entries → NaN.
    - fix wrong NaN values anything resembling "in" ("___", "[]", "\nNone\n \n", "none", 9999, 999, -1, 'None', 'NA', "n/a", "Unknown","UNK", "null", "NULL", ".", " ", ... problematic tokens:
    '___': 68645
    'ART.': 6348
    'NEG': 4234
    'MIX.': 2173
    'NONE': 2070 (false NA)
    'INTUBATED.': 1576
    'VEN.': 1476
    'NOT INTUBATED.': 686
    'CONTROLLED.': 684
    '0-2': 585)
    - Antibiotic dilution_values outside known MIC range → drop or cap
    - Use domain-specific limits (e.g., glucose > 2000 → impossible)
    - Check that charttime always precedes dod
    - Identify admissions with no labs / no notes / no procedures (important for clustering completeness).

- identify and handle individually missing values (NaNs)
    - dod: nan means not dead: keep separate; convert afterward → derive is_dead

- cleaning / reducing:
    - Standardize boolean indicator columns (ECG, CT, MRI, etc.) to {0,1}.
    - remove columns irrelevant for clustering (raw text) - which ones?
    - icd_code mapping to fewer broad categories as a new variable (ICD hierarchy output features (chapters, blocks, counts))
    - Unit normalization for labs dataset!!
    - Antibiotic interpretation rules in microbiology
    - Text column handling strategy

Ensuring consistency of demographics across notes

- check and handle duplicated records - Use subset-level duplicates:
    - Heart Diagnoses: (note_id)
    - labs: (hadm_id, charttime, label)
    - Microbiology: (hadm_id, charttime, test_name, spec_type_desc)
    - Procedures: (hadm_id, chartdate, icd_code)

- check and handle outliers . (e.g. using visualization technique pearson, corr, scatter (3d also), parallel plot, histogram, boxplot, z-score.. ) 

**Step 2:** Add subject_id to missing DF2 by merging with DF1&DF3&D4

**Step 3:** Compute admission-level features via groupby(['subject_id', 'hadm_id'])
- Sort events by time within each admission
- Standardize units (mg/dL, mmol/L confusion in labs)
- Create derived boolean flags (e.g., “organism_detected”, “abnormal_flag_ratio”)


**Step 4:** Merge admission-level feature tables using how='inner' on=['subject_id','hadm_id']
Data completeness audit before merging: Compute completeness matrix per admission ( decide whether to exclude sparse admissions before clustering)
- has_notes (0/1)
- has_labs (0/1)
- has_micro (0/1)
- has_procedures (0/1)    

**Step 5:** Aggregate all admission-level features to patient-level groupby('subject_id')

**Step 6**: Normalize
- Scaling numeric variables (z-scaling, keep)
- Encoding categorical variables
- Log-transform extreme skewed labs
