GOAL is to create a subject profile with about ~10 features in the end:

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
What chatty said:
- Use a reference table (e.g., Diagnoses) with both hadm_id + subject_id.
- For datasets with only hadm_id, merge with reference to add subject_id.
- Compute all features per admission (hadm_id, subject_id).
- Merge datasets on both keys (hadm_id, subject_id) to keep integrity.

Finally, aggregate by subject_id to build patient-level profiles.
1.2 data preparation
prof notes:
Improve the quality of your data and prepare it by extracting new features interesting
for describing the patients. Therefore, you are going to describe the information
patient wise and examples of indicators to be computed are:
● Highest value of glucose recorded for the patient during the admission?
● Total count of laboratory events linked to the admission?
● Ratio between the number of tests flagged as abnormal and the total number
of tests?
● Total count of microbiology examinations for the admission?
● Total count of procedure codes linked to the admission?
Note that these examples are not mandatory. You can derive indicators that you
prefer and that you consider interesting for describing the patients.
It is MANDATORY that each team defines some indicators. Each of them has to be
correlated with a description (in which should be clearly stated the objective of the
variable derived) and when it is necessary also its mathematical formulation.
The extracted variables will be useful for the clustering analysis (i.e., the second
project’s task). Once the set of indicators is computed, the team has to explore the
new features for a statistical analysis (distributions, outliers, visualizations,
correlations).
Subtasks of Data Understanding:
● Data semantics for each feature (min, max, avg, std) above and the new one
defined by the team
● Distribution of the variables and statistics
● Assessing data quality (missing values, outliers, duplicated records, errors)
● Variables transformations
● Pairwise correlations and eventual elimination of redundant variables.
Nice visualization and insights can be obtained, explore the web to get more ideas!
Please add these substaks in your final report.

My todo items:
1.2.1 Transformations, NaN removal, otulier handling  

- z normalization per col
- outlier to remove?
- remove qc_flag == FAIL

1.2.2 Feature engineering - create one feature per dataset at least
-

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
