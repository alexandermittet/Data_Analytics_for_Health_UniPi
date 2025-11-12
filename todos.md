GOAL is to create a subject profile with about ~10 feaut in the end:

1.1:
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
1.2
1.2.1 Transformations, NaN removal, otulier handling  
- z normalization per col
- outlier to remove?
- remove qc_flag == FAIL

1.2.2 Feature engineering - create one feature per dataset at least!
- 
- per subject_id: time since last admission 
- per subject_id: total admission  
- DONE Total count of laboratory events linked to the admission
- DONE ratio between the number of tests flagged as abnormal and the total number 
of tests?
- think of more features (one for each df at least)

2. clustering

3. time series