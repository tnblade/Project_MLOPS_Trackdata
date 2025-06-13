import joblib
import pandas as pd
import json
from datetime import datetime
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, Field
import shap
import os
import time
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(
    title="Customer Churn Prediction API 🚀",
    description="💡 API dự đoán khả năng khách hàng rời đi.",
    version="1.0.0"
)

instrumentator = Instrumentator()

# Sau khi tạo app FastAPI:
instrumentator.instrument(app).expose(app)
# Cài đặt các thư viện cần thiết

# Load mô hình và preprocessor
model = joblib.load("models/model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# Khởi tạo SHAP Explainer
explainer = shap.TreeExplainer(model)

# Khởi tạo FastAPI


# Định nghĩa schema dữ liệu đầu vào và đầu ra
class PredictionResponse(BaseModel):
    churn: int
    churn_probability: float

class Customer(BaseModel):
    gender: str = Field(..., example="Female")
    SeniorCitizen: int = Field(..., example=0)
    Partner: str = Field(..., example="Yes")
    Dependents: str = Field(..., example="No")
    tenure: int = Field(..., example=12)
    PhoneService: str = Field(..., example="Yes")
    MultipleLines: str = Field(..., example="No")
    InternetService: str = Field(..., example="Fiber optic")
    OnlineSecurity: str = Field(..., example="No")
    OnlineBackup: str = Field(..., example="Yes")
    DeviceProtection: str = Field(..., example="Yes")
    TechSupport: str = Field(..., example="No")
    StreamingTV: str = Field(..., example="Yes")
    StreamingMovies: str = Field(..., example="Yes")
    Contract: str = Field(..., example="Month-to-month")
    PaperlessBilling: str = Field(..., example="Yes")
    PaymentMethod: str = Field(..., example="Electronic check")
    MonthlyCharges: float = Field(..., example=75.3)
    TotalCharges: float = Field(..., example=1234.56)

# Ghi log input + output để theo dõi drift hoặc phục vụ monitoring
def log_input_output(input_data, prediction, proba, inference_time=None):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": input_data,
        "prediction": int(prediction),
        "probability": float(round(proba, 4))
    }
    if inference_time is not None:
        log["inference_time"] = inference_time
    os.makedirs("logs", exist_ok=True)
    with open("logs/prediction_log.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")
# Đảm bảo thư mục logs tồn tại
os.makedirs("logs", exist_ok=True)
# Ghi log mô hình và preprocessor
with open("logs/model_info.txt", "w") as f:
    f.write(f"Model: {model.__class__.__name__}\n")
    f.write(f"Preprocessor: {preprocessor.__class__.__name__}\n")
    f.write(f"Timestamp: {datetime.utcnow().isoformat()}\n")
# Ghi log SHAP explainer
with open("logs/shap_info.txt", "w") as f:
    f.write(f"SHAP Explainer: {explainer.__class__.__name__}\n")
    f.write(f"Model: {model.__class__.__name__}\n")
    f.write(f"Timestamp: {datetime.utcnow().isoformat()}\n")

# Ghi log thông tin mô hình và preprocessor 

# Route dự đoán
@app.post("/predict", response_model=PredictionResponse)
def predict(data: Customer):
    start = time.time()
    df = pd.DataFrame([data.dict()])
    X = preprocessor.transform(df)
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1]
    inference_time = time.time() - start

    # Log thêm inference time nếu muốn
    log_input_output(data.dict(), pred, proba, inference_time)

    return {
        "churn": int(pred),
        "churn_probability": round(proba, 3)
    }
# Route giải thích mô hình bằng SHAP
@app.post("/explain")
def explain(data: Customer):
    df = pd.DataFrame([data.dict()])
    X = preprocessor.transform(df)
    shap_values = explainer.shap_values(X)
    explanation = dict(zip(df.columns, shap_values[1][0].tolist()))
    return {
        "explanation": explanation,
        "expected_value": explainer.expected_value[1]
    }
# Hàm chạy dvc repro retrain_model
def run_dvc_repro():
    os.system("dvc repro retrain_model")

# Route trigger retrain
@app.post("/retrain")
def retrain(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_dvc_repro)
    return {"message": "Retrain triggered"}

# Chạy bằng uvicorn khi phát triển local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
# Chạy bằng gunicorn khi deploy
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker api:app --bind