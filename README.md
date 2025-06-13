# 🔍 Customer Churn Prediction - ML Pipeline Production

## 🚀 Giới thiệu dự án

Dự án xây dựng pipeline machine learning hoàn chỉnh để **dự đoán khả năng rời bỏ dịch vụ của khách hàng**, bao gồm:

- ✅ Data & Model Versioning (DVC)
- ✅ Experiment Tracking (MLflow)
- ✅ Hyperparameter Tuning (Optuna)
- ✅ Drift Detection
- ✅ Triển khai mô hình với FastAPI
- ✅ Monitoring & Logging (Prometheus, Grafana, Alertmanager)
- ✅ Có thể mở rộng với CI/CD (GitHub Actions)

> 🎯 **Mục tiêu**: Xây dựng pipeline dễ mở rộng & tái sử dụng, sẵn sàng triển khai trong môi trường production.

---

## 💡 Điểm nổi bật

| Tính năng | Mô tả |
|----------|-------|
| **DVC** | Quản lý pipeline và version dữ liệu, model |
| **MLflow** | Theo dõi toàn bộ thông số huấn luyện, metric và artifact |
| **Optuna** | Tự động tìm hyperparameter tối ưu |
| **FastAPI** | Cung cấp API dự đoán |
| **Prometheus + Grafana** | Giám sát tài nguyên hệ thống, mô hình & API |
| **Alertmanager** | Gửi cảnh báo nếu có bất thường |

---

## 🧱 Công nghệ sử dụng

| Công nghệ     | Vai trò |
|---------------|---------|
| Python ≥ 3.8  | Ngôn ngữ chính |
| scikit-learn  | Huấn luyện mô hình |
| DVC           | Quản lý pipeline & model |
| MLflow        | Theo dõi quá trình training |
| Optuna        | Hyperparameter tuning |
| FastAPI       | Triển khai API dự đoán |
| Prometheus    | Thu thập metrics |
| Grafana       | Dashboard trực quan |
| Alertmanager  | Hệ thống cảnh báo |
| Docker        | Đóng gói & triển khai dịch vụ |

---

## 🔧 Cài đặt môi trường (Chạy Local thủ công)

### 1. Tạo môi trường
conda create -n churn_env python=3.9
conda activate churn_env

### 2. Cài thư viện
pip install --upgrade pip
pip install -r requirements.txt

## Chạy pipeline từng bước

### 1. Tiền xử lý dữ liệu
python scripts/data_load.py

### 2. Tìm hyperparameters tốt nhất
python scripts/hyperparameter.py

### 3. Huấn luyện mô hình
python scripts/train.py

### 4. Đánh giá mô hình
python scripts/evaluate.py

### 5. Phát hiện data drift
python scripts/drift_detect.py

### Theo dõi thí nghiệm

mlflow ui

Truy cập: http://localhost:5000

### Dự đoán với FastAPI

uvicorn scripts.api:app --reload

Truy cập docs: http://localhost:8000/docs

## Triển khai với Docker

### 1. Tạo môi trường (chỉ lần đầu)

conda create -n churn_env python=3.9

conda activate churn_env

pip install -r requirements.txt

### 2. Build & Chạy toàn bộ hệ thống

docker-compose up --build

## Truy cập các dịch vụ
Dịch vụ	Đường dẫn
🔗 FastAPI:	http://localhost:8000/docs
📊 Prometheus:	http://localhost:9090
📉 Grafana:	http://localhost:3000
🖥️ Node Exporter:	http://localhost:9100
📦 cAdvisor (monitor container):	http://localhost:8080

## Cảnh báo hệ thống (Alertmanager)

Dự án tích hợp Alertmanager để gửi cảnh báo khi:

❌ Tốc độ phản hồi API cao bất thường

❌ Tỷ lệ lỗi vượt quá 50%

❌ Confidence score < 0.6

❌ CPU > 90%

## Cấu hình email cảnh báo:

### Điền thông tin vào .env:


SMTP_FROM=your_email@gmail.com
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAIL_TO=recipient_email@gmail.com

### Khởi chạy Alertmanager (tự động qua docker-compose)
