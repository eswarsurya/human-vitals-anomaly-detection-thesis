# Human Vitals Anomaly Detection Thesis

**Status: Completed MSc Data Analytics thesis project**

Machine learning thesis project focused on detecting unusual human vital-sign patterns and explaining why each record is flagged. The project combines a large multivariate dataset, unsupervised anomaly detection, explainable AI, and documented analytical reporting.

## Why This Project Matters

A useful anomaly detector should not only identify unusual records. Analysts and stakeholders also need to understand which measurements contributed to the decision. This project addresses that problem using **Isolation Forest** and **SHAP explainability**.

The completed thesis workflow covers **200,020 human vital-sign records**.

## Analytics Question

Can an unsupervised machine-learning workflow identify unusual vital-sign patterns and provide explanations that are clear enough for analytical review?

## Tools Used

Python, Pandas, NumPy, Scikit-learn, Isolation Forest, SHAP, Matplotlib, Seaborn, Jupyter Notebook, Word, and PowerPoint.

## What I Implemented

- Cleaned and prepared multivariate vital-sign data.
- Built an Isolation Forest workflow for anomaly detection.
- Used SHAP values to explain feature contribution to anomaly decisions.
- Produced public-safe anomaly, risk-category, gender-distribution, and summary outputs.
- Documented methodology, assumptions, limitations, and interpretation.
- Added a reusable Python pipeline and public notebook for review.

## Key Evidence

- **200,020 records** in the full project dataset.
- **Isolation Forest** used for unsupervised anomaly detection.
- **SHAP** used to explain anomaly drivers.
- Public-safe outputs and sample data provided for GitHub review.

The project deliberately avoids publishing the raw dataset because it contains record identifiers and exact timestamps.

## Repository Guide

| Path | Purpose |
| --- | --- |
| `data/` | Public-safe sample and sharing notes |
| `outputs/` | Dataset profile, summaries, distributions, and model output |
| `src/` | Reusable anomaly detection pipeline |
| `notebooks/` | Public workflow notebook and analysis |
| `project-evidence/` | Report summary and walkthrough |
| `reports/` | Public-safe thesis documentation |
| `assets/` | Aggregate visuals |

## How To Review

Start with `outputs/model_output_summary.md`, then inspect `src/anomaly_detection_pipeline.py`, `notebooks/human_vitals_public_workflow.ipynb`, and `project-evidence/report_summary.md`.

## Related Engineering Project

The thesis modelling approach was also extended into a service-oriented API:

[Human Vitals Anomaly Detection API](https://github.com/eswarsurya/human-vitals-anomaly-api)

## Author

**Eswar Surya Danaboina** · MSc Data Analytics · Dublin, Ireland

Portfolio: https://eswardanaboina.vercel.app/  
LinkedIn: https://www.linkedin.com/in/eswarsurya76/
