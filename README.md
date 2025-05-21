<<<<<<< HEAD
# Project_MLOPS_Trackdata
=======
# 🧠 Telco Customer Churn MLOps Pipeline with DVC, MLflow, Optuna

## 🚀 Giới thiệu dự án

Dự án này xây dựng một pipeline hoàn chỉnh cho bài toán dự đoán **Telco Customer Churn** từ dữ liệu Kaggle. Pipeline đáp ứng các tiêu chuẩn của **MLOps hiện đại** với:

- Data & Model Versioning (DVC)
- Experiment Tracking (MLflow)
- Hyperparameter Tuning (Optuna)
- Drift Detection
- CI/CD (có thể mở rộng với GitHub Actions)
- Triển khai mô hình với FastAPI (có thể nâng cấp thêm Prometheus + Grafana)

> 🎯 Mục tiêu: Dự đoán khách hàng có rời bỏ dịch vụ hay không, triển khai pipeline dễ mở rộng & tái sử dụng trong môi trường production.

---

## 🔧 Pipeline gồm những gì?

## 📁 Cấu trúc dự án

├── .github/
│   └── workflows/
│       └── ci-cd.yml               # GitHub Actions CI/CD
├── data/                          # Thư mục chứa dữ liệu
│   ├── raw/                       # Dữ liệu gốc tải từ Kaggle
│   └── processed/                 # Dữ liệu đã xử lý và sẵn sàng cho training
│
├── models/                        # Chứa mô hình đã huấn luyện và preprocessor
│   ├── model.pkl                  # Mô hình đã huấn luyện (Random Forest)
│   └── preprocessor.pkl           # Preprocessor cho dữ liệu (scaler, encoder, etc.)
│
├── scripts/                       # Thư mục chứa các script cho các bước trong pipeline
│   ├── data_load.py               # Xử lý và tải dữ liệu
│   ├── evaluate.py                # Đánh giá mô hình
│   ├── hyperparameter.py          # Tuning hyperparameter với Optuna
│   ├── mlflow_logging.py                 # Log các thông số và kết quả vào MLflow
│   ├── train.py                   # Huấn luyện mô hình và log kết quả
│   └── drift_detect.py            # Phát hiện drift của dữ liệu (drift detection)
|   └── api.py                       # FastAPI API
├── tests/
│   └── test_api.py
├── Dockerfile 
├── dvc.yaml
├── params.yaml                         # (tuỳ chọn) cho tuning, configs
├── requirements.txt
└── README.md



## 💡 Điểm nổi bật & sáng tạo

- ✅ **Tự động hoá toàn bộ quy trình training** thông qua `dvc.yaml`
- ✅ **Tracking toàn bộ thí nghiệm** bằng MLflow (params, metrics, artifact)
- ✅ **Tuning tự động** bằng Optuna + log lại vào MLflow
- ✅ **Xử lý drift dữ liệu** để kiểm tra nếu mô hình cần retrain
- ✅ Dễ dàng mở rộng với GitHub Actions, Prometheus, Grafana, FastAPI
- ✅ Thân thiện khi cộng tác nhóm (DVC hỗ trợ push/pull dữ liệu & model)

---

## ⚙️ Framework & Công nghệ sử dụng

| Công nghệ     | Mục đích |
|---------------|---------|
| **DVC**       | Pipeline orchestration & version control (dữ liệu & model) |
| **MLflow**    | Theo dõi thí nghiệm: hyperparams, metrics, artifact |
| **Optuna**    | Tối ưu hoá hyperparameters |
| **scikit-learn** | Huấn luyện model Random Forest |
| **FastAPI**   | (có thể triển khai) API dự đoán mô hình |
| **joblib**    | Lưu mô hình & pipeline |
| **Pandas/Numpy** | Xử lý dữ liệu |
| **Python ≥ 3.8** | Ngôn ngữ chính |

---

## 🛠️ Hướng dẫn cài đặt setup trên máy


✅ 1. Tải dataset từ Kaggle lưu trong raw

WA_Fn-UseC_-Telco-Customer-Churn.csv  #🔗 Link: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### 1. tai requirement
conda create name_env python3.9

conda activate name_env

python.exe -m pip install --upgrade pip

pip install -r requirements.txt

▶️ Cách chạy pipeline

1. Tiền xử lý dữ liệu

python scripts/data_load.py

2. Tim best parameter

python scripts/hyperparameter.py

3. Huấn luyện mô hình

python scripts/train.py

4. Đánh giá mô hình

python scripts/evaluate.py

5. Phát hiện drift dữ liệu

python scripts/drift_detect.py

6. Theo dõi MLflow

mlflow ui
7. deploy fastAPI
python scripts/api.py

# Truy cập tại: http://localhost:5000

🛠️ Sử dụng DVC (thay vì chạy từng bước như trên)
# Khởi tạo DVC
dvc init

# Thêm remote để lưu trữ model/data
dvc remote add -d myremote gdrive://<your-id> 

# Theo dõi file raw
dvc add data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv

# create a .gitignore file if which does not exists
echo ".dvc/cache/" > .gitignore
echo ".dvc/tmp/" >> .gitignore
echo "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv" >> .gitignore

# Commit tracking file
git add data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv.dvc .gitignore
git commit -m "Track raw dataset with DVC"

# Chạy toàn bộ pipeline

dvc repro

# Quản lý model/data với DVC remote

# Push model và data lên remote
dvc push

# Khi clone repo trên máy khác:
git clone <repo>
cd <repo>
dvc pull

>>>>>>> fd2b540 (Initial commit)
