import pandas as pd
import numpy as np

diagnoses = "./Data 2/heart_diagnoses_1.csv"
final_labels   = "subject_to_labels_ischemic.csv"

def compute_ischemic_label(code_set: set) -> int:
    ischemic = len(code_set & class1) > 0
    return 1 if ischemic else 0

icds = {
    "I20", "I21", "I22", "I24", "I25",
    "I30", "I31", "I33",
    "I34", "I35", "I36",
    "I40", "I42",
    "I44", "I45", "I46", "I47", "I48", "I49",
    "I50"
}

class1 = {"I20", "I21", "I22", "I24", "I25"}

diag = pd.read_csv(diagnoses)

diag["subject_id"] = diag["subject_id"].astype(str).str.strip()
diag["icd_code"] = (
    diag["icd_code"]
    .astype(str)
    .str.strip()
    .str.upper()
    .replace({"": np.nan, "NAN": np.nan})
)


diag_valid = diag[diag["icd_code"].isin(icds)].copy()
if diag_valid.empty:
    raise ValueError("Problems with the format of the codes")

subject_codes = (
    diag_valid.groupby("subject_id")["icd_code"].unique().reset_index(name="icd_codes_list")
)
subject_codes["icd_codes_set"] = subject_codes["icd_codes_list"].apply(set)
print(subject_codes)

subject_codes["label_ischemic"] = subject_codes["icd_codes_set"].apply(compute_ischemic_label)

subject_codes.drop(['icd_codes_list','icd_codes_set'], axis=1, inplace=True)


subject_codes.to_csv(final_labels, index=False)
print(subject_codes["label_ischemic"].value_counts())
