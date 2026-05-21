# Model Output Summary

This file gives a public, recruiter-friendly view of the thesis output without exposing the full raw dataset.

## Project Output

The thesis workflow detects unusual human vital-sign records using an unsupervised anomaly detection approach. The key output is a set of flagged records, supporting visual summaries, and SHAP-based explanations showing which variables influenced the anomaly decision.

## Main Evidence

- Dataset scale: 200020 vital-sign records.
- - Modelling approach: Isolation Forest.
  - - Explainability approach: SHAP values.
    - - Output type: anomaly flags, anomaly drivers, and visual model review.
     
      - ## Interpretation
     
      - The project focuses on trust and explainability. Instead of only producing a model score, the work explains why a record appears unusual, making the output easier to review and discuss.
     
      - ## Public Sharing Note
     
      - The raw dataset is not uploaded until privacy and sharing suitability are confirmed. A small synthetic or anonymised sample can be added later.
      - 
