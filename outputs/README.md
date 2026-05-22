# Public Output Evidence

This folder contains public-safe output evidence for the Human Vitals Anomaly Detection thesis project.

## Files

- `dataset_profile.csv` summarises the dataset size and confirms that the raw dataset is not uploaded.
- `risk_category_distribution.csv` summarises the risk category distribution.
- `gender_distribution.csv` summarises the gender distribution.
- `vital_sign_summary_statistics.csv` gives descriptive statistics for public-safe numeric fields.
- `model_output_summary.md` explains the anomaly detection and SHAP output without exposing raw records.

## Privacy Note

The raw dataset contains direct record identifiers and exact timestamps. For public GitHub review, only a small sample without those fields is prepared.
