import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def load_vitals_data(path):
      """Load a public-safe or local vital-sign dataset."""
      return pd.read_csv(path)


def prepare_features(df, feature_columns):
      """Select numeric vital-sign features and scale them for modelling."""
      features = df[feature_columns].copy()
      features = features.dropna()
      scaler = StandardScaler()
      scaled = scaler.fit_transform(features)
      return features, scaled, scaler


def train_anomaly_model(scaled_features, contamination=0.05, random_state=42):
      """Train an Isolation Forest model for unsupervised anomaly detection."""
      model = IsolationForest(
          n_estimators=200,
          contamination=contamination,
          random_state=random_state
      )
      model.fit(scaled_features)
      return model


def score_anomalies(features, scaled_features, model):
      """Return anomaly labels and scores for review."""
      output = features.copy()
      output["anomaly_label"] = model.predict(scaled_features)
      output["anomaly_score"] = model.decision_function(scaled_features)
      output["is_anomaly"] = output["anomaly_label"].map({1: 0, -1: 1})
      return output


if __name__ == "__main__":
      print("Use this script with a public-safe vital-sign sample dataset.")
      print("Example workflow: load data, prepare features, train model, score anomalies.")
  
