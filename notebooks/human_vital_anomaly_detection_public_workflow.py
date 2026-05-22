"""Public-safe workflow for the Human Vitals Anomaly Detection thesis.

This script mirrors the main thesis process without exposing the raw dataset.
The public sample removes direct patient IDs and exact timestamps.
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler

DATA_PATH = "../data/public_sample_human_vitals.csv"
NON_NUMERIC_COLUMNS = ["sample_record", "Gender", "Risk Category"]


def load_data(path=DATA_PATH):
    """Load the public-safe sample dataset."""
    return pd.read_csv(path)


def prepare_features(df):
    """Prepare numeric vital-sign fields for anomaly detection."""
    numeric_data = df.drop(columns=NON_NUMERIC_COLUMNS, errors="ignore")
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(numeric_data)
    return numeric_data, scaled, scaler


def train_isolation_forest(scaled_features, contamination=0.05):
    """Train the Isolation Forest model used for anomaly detection."""
    model = IsolationForest(
        n_estimators=300,
        contamination=contamination,
        random_state=42,
    )
    model.fit(scaled_features)
    return model


def score_records(df, model, scaled_features):
    """Attach anomaly labels and anomaly scores to the reviewed records."""
    scored = df.copy()
    scored["anomaly"] = model.predict(scaled_features)
    scored["anomaly_score"] = model.decision_function(scaled_features)
    return scored


if __name__ == "__main__":
    vitals = load_data()
    features, scaled_features, fitted_scaler = prepare_features(vitals)
    anomaly_model = train_isolation_forest(scaled_features)
    scored_vitals = score_records(vitals, anomaly_model, scaled_features)

    total_records = len(scored_vitals)
    anomaly_count = int((scored_vitals["anomaly"] == -1).sum())
    anomaly_rate = round((anomaly_count / total_records) * 100, 2)

    print(f"Reviewed records: {total_records}")
    print(f"Anomalies detected: {anomaly_count}")
    print(f"Anomaly rate: {anomaly_rate}%")
