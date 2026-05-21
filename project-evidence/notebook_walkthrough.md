# Notebook Walkthrough

This file explains the expected workflow of the Human Vitals Anomaly Detection notebook in a public-friendly format.

## 1. Data Preparation

The notebook begins by loading the human vital-sign dataset, checking structure, reviewing missing values, and preparing numeric health measurements for modelling.

## 2. Exploratory Review

The analysis reviews vital-sign distributions and looks for unusual ranges or patterns that may affect anomaly detection.

## 3. Model Development

The core model uses Isolation Forest to identify records that behave differently from the wider dataset. This is useful when labelled anomaly examples are not available.

## 4. Explainability

SHAP is used to make the anomaly output easier to understand. The goal is to show which vital-sign variables contributed to a record being considered unusual.

## 5. Output Review

The notebook output is designed to support review of anomaly flags, anomaly drivers, visual summaries, and model behaviour.

## 6. Communication

The results are documented in a report and presentation so the technical workflow can be explained clearly to non-technical stakeholders.
