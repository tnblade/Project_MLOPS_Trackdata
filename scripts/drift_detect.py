import numpy as np
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import joblib
import os
import pandas as pd
import json
import requests

DRIFT_THRESHOLD = 0.3  # Ngưỡng drift tùy chỉnh

def load_drift_score(json_path):
    with open(json_path, "r") as f:
        report_json = json.load(f)
    
    # Lấy drift score từ json (cách lấy tùy thuộc cấu trúc Evidently report)
    # Ví dụ lấy dataset_drift từ phần "metrics"
    metrics = report_json.get("metrics", [])
    for metric in metrics:
        if metric.get("name") == "DatasetDrift":
            return metric.get("result", {}).get("dataset_drift", 0)
    return 0

def main():
    print("Loading processed data and preprocessor...")
    
    if not os.path.exists("data/processed/train.npz") or not os.path.exists("data/processed/test.npz"):
        raise FileNotFoundError("Processed data files not found. Run `data_load.py` first.")

    if not os.path.exists("models/preprocessor.pkl"):
        raise FileNotFoundError("Preprocessor not found. Ensure preprocessing has run successfully.")

    # Load data
    train = np.load("data/processed/train.npz")
    test = np.load("data/processed/test.npz")
    preprocessor = joblib.load("models/preprocessor.pkl")

    X_train = train["X"]
    X_test = test["X"]

    feature_names = preprocessor.get_feature_names_out()
    X_train_df = pd.DataFrame(X_train, columns=feature_names)
    X_test_df = pd.DataFrame(X_test, columns=feature_names)

    print("Running Data Drift Report...")
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=X_train_df, current_data=X_test_df)

    os.makedirs("reports", exist_ok=True)
    report_html_path = "reports/drift_report.html"
    report_json_path = "reports/drift_report.json"
    report.save_html(report_html_path)
    report.save_json(report_json_path)

    print(f"Drift report saved at: {report_html_path} and {report_json_path}")

    # Đọc drift score từ file json
    drift_score = load_drift_score(report_json_path)
    print(f"Detected drift score: {drift_score}")

    if drift_score > DRIFT_THRESHOLD:
        print("Drift detected! Triggering retrain pipeline...")

        try:
            response = requests.post("http://localhost:5000/retrain")
            if response.status_code == 200:
                print("Retrain webhook triggered successfully.")
            else:
                print(f"Failed to trigger retrain webhook. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error triggering retrain webhook: {e}")

if __name__ == "__main__":
    main()
