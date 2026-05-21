# Human Vitals Anomaly Detection Thesis

Machine learning thesis project focused on detecting unusual human vital sign patterns and explaining why each record is flagged. This is one of my strongest academic projects because it combines a large dataset, unsupervised modelling, explainable AI, and clear reporting.

## Why This Project Matters

In healthcare style analytics, a model should not only say that something looks unusual. Analysts and stakeholders also need to understand which measurements influenced that decision. This project was built to explore that problem using anomaly detection and SHAP explainability.

The work was completed as part of my MSc Data Analytics study and uses 200020 human vital sign records.

## Analytics Question

Can an unsupervised machine learning model identify unusual vital sign patterns, and can the output be explained clearly enough for review and trust?

## Tools Used

Python, Pandas, NumPy, Scikit learn, Isolation Forest, SHAP, Matplotlib, Seaborn, Jupyter Notebook, Word, and PowerPoint.

## What I Implemented

I cleaned and prepared multivariate vital sign data for anomaly detection. I built an Isolation Forest workflow to identify unusual records, then used SHAP values to explain which features contributed to anomaly decisions. I also created visual analysis to compare normal and anomalous patterns, and documented the methodology, assumptions, results, and limitations in a thesis style report.

## Repository Guide

The notebooks folder is for the model workflow and analysis notebook. The reports folder is for the thesis report and presentation. The data folder is for dataset notes and access guidance. The requirements file lists the Python libraries used.

## Outputs And Results

The project produced a working anomaly detection process for large vital sign data, explainability output showing drivers behind anomaly scores, visual summaries for reviewing model behaviour, and a report and presentation suitable for academic and recruiter review.

## How Recruiters Should Review This

Start with this README to understand the purpose. Then review the notebook for the technical workflow and the report for methodology, interpretation, and written communication. This project demonstrates applied machine learning, explainable AI, and the ability to communicate model results clearly.

## Next Improvements

I plan to add a smaller public sample dataset for reproducible review, include dashboard screenshots from the model output, and add a short model evaluation summary table for faster recruiter scanning.
