# Human Vitals Anomaly Detection Thesis

Machine learning thesis project focused on detecting unusual human vital-sign patterns and explaining why each record is flagged. This is one of my strongest academic projects because it combines a large dataset, unsupervised modelling, explainable AI, and clear reporting.

## Why This Project Matters

In healthcare-style analytics, a model should not only say that something looks unusual. Analysts and stakeholders also need to understand which measurements influenced that decision. This project explores that problem using anomaly detection and SHAP explainability.

The work was completed as part of my MSc Data Analytics study and uses **200,020 human vital-sign records**.

## Analytics Question

Can an unsupervised machine learning model identify unusual vital-sign patterns, and can the output be explained clearly enough for review and trust?

## Tools Used

Python, Pandas, NumPy, Scikit-learn, Isolation Forest, SHAP, Matplotlib, Seaborn, Jupyter Notebook, Word, and PowerPoint.

## What I Implemented

I cleaned and prepared multivariate vital-sign data for anomaly detection. I built an Isolation Forest workflow to identify unusual records, then used SHAP values to explain which features contributed to anomaly decisions. I also created visual analysis to compare normal and anomalous patterns, and documented the methodology, assumptions, results, and limitations in a thesis-style report.

## Repository Guide

| Path | Purpose |
|---|---|
| `data/` | Public-safe sample data and dataset sharing notes. |
| `outputs/` | Dataset profile, summary statistics, risk/gender distributions, and model output summary. |
| `src/` | Reusable Python anomaly detection pipeline. |
| `notebooks/` | Public workflow script and notebook walkthrough material. |
| `project-evidence/` | Report summary and notebook walkthrough written for public review. |
| `reports/` | Notes for public-safe thesis report and presentation evidence. |
| `assets/` | Public-safe visuals created from aggregate outputs. |

## Public Evidence Added

- Public-safe sample dataset with direct patient identifiers and exact timestamps removed.
- Dataset profile confirming the full project scale of 200,020 records.
- Summary statistics for the public-safe vital-sign fields.
- Risk category and gender distribution output files.
- Public Python workflow showing the Isolation Forest process.
- Report summary, notebook walkthrough, and model output summary.
- Simple aggregate visuals for quick review.

## Outputs And Results

The project produced a working anomaly detection process for large vital-sign data, explainability output showing drivers behind anomaly scores, visual summaries for reviewing model behaviour, and a report and presentation suitable for academic review.

The public GitHub version avoids uploading the raw dataset because it contains record identifiers and exact timestamps. Instead, it includes safe sample data and aggregate evidence that demonstrates the project structure and output.

## Project Walkthrough

A good way to explore this project is to start with the README, then review `outputs/model_output_summary.md`, `project-evidence/report_summary.md`, and `notebooks/human_vital_anomaly_detection_public_workflow.py`. The project is intended to show applied machine learning, explainable AI, and clear communication of model results.

## Next Improvements

Planned improvements include exporting the final thesis report as a clean public PDF and adding screenshots from SHAP/model visuals where sharing is appropriate.
