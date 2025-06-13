
## 🚀 Giới thiệu dự án
- Data & Model Versioning (DVC)
- Experiment Tracking (MLflow)
- Hyperparameter Tuning (Optuna)
- Drift Detection
- CI/CD (có thể mở rộng với GitHub Actions)
- Triển khai mô hình với FastAPI (có thể nâng cấp thêm Prometheus + Grafana)
> 🎯 Mục tiêu: Dự đoán khách hàng có rời bỏ dịch vụ hay không, triển khai pipeline dễ mở rộng & tái sử dụng trong môi trường production.

## 💡 Điểm nổi bật & sáng tạo

- ✅ **Tự động hoá toàn bộ quy trình training** thông qua `dvc.yaml`
- ✅ **Tracking toàn bộ thí nghiệm** bằng MLflow (params, metrics, artifact)
- ✅ **Tuning tự động** bằng Optuna + log lại vào MLflow
- ✅ **Xử lý drift dữ liệu** để kiểm tra nếu mô hình cần retrain
- ✅ Dễ dàng mở rộng với GitHub Actions, Prometheus, Grafana, FastAPI
- ✅ Thân thiện khi cộng tác nhóm (DVC hỗ trợ push/pull dữ liệu & model)

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

## Link gdrive show video demo: https://drive.google.com/drive/folders/1v-Cm9WxO3KSNequrqD9mSdlblWjfY6Hk?usp=sharing

## 🛠️ Hướng dẫn cài đặt setup trên máy (local chạy thủ công)

1. setup môi trường

conda create name_env python3.9

conda activate name_env

python.exe -m pip install --upgrade pip

pip install -r requirements.txt

2. Tiền xử lý dữ liệu

python scripts/data_load.py

3. Tim best parameter

python scripts/hyperparameter.py

4. Huấn luyện mô hình

python scripts/train.py

5. Đánh giá mô hình

python scripts/evaluate.py

6. Phát hiện drift dữ liệu

python scripts/drift_detect.py

7. Theo dõi MLflow

mlflow ui

8. fastAPI
   
uvicorn scripts.api:app --reload

Truy cập: http://localhost:8000/docs

## Hướng dẫn Deploy model với Docker (lưu ý mở Docker Desktop)

1. setup môi trường
   
conda create name_env python3.9

conda activate name_env

python.exe -m pip install --upgrade pip

pip install -r requirements.txt

2. Deploy API bằng Docker

docker-compose up --build

3. Truy cập các công cụ


FastAPI:	http://localhost:8000/docs

Prometheus:	http://localhost:9090

Grafana:	http://localhost:3000

Node Exporter:	http://localhost:9100

cAdvisor:	http://localhost:8080




