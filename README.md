# ⚽ Athlete Readiness Modeling with Personalized Baselines and Workload Anomaly Detection

## 📌 Project Overview

The Athlete Readiness system is a data science prototype designed to help football coaches and performance analysts monitor athlete readiness, training workload, recovery, performance trends, and unusual workload patterns.

The system combines data analytics, personalized workload baselines, anomaly detection, machine learning, a FastAPI backend, and a Streamlit dashboard.

---

## 🎯 Objectives

- Monitor athlete training workload and performance.
- Calculate personalized workload baselines.
- Detect unusual workload patterns using statistical anomaly detection.
- Generate an athlete readiness score.
- Analyze recovery and sleep indicators.
- Provide visual insights through an interactive dashboard.
- Provide athlete analytics through a FastAPI service.
- Compare baseline and improved machine learning approaches.
- Provide model explainability using permutation importance.
- Include data validation, testing, logging, and deployment documentation.

---

## 🏗️ System Architecture

```text
Athlete Session Data
        ↓
Data Validation
        ↓
Analytics Pipeline
        ↓
Workload & Recovery Features
        ↓
Personalized Baseline
        ↓
Anomaly Detection
        ↓
Readiness Scoring
        ↓
Machine Learning
        ↓
FastAPI Backend
        ↓
Streamlit Dashboard
        ↓
Coach / Performance Analyst

📊 Dataset

The project uses a realistic synthetic football athlete-session dataset.

Each row represents one athlete training session.

Main attributes include:

Athlete ID
Age
Position
Date
Session Type
Session Duration
Distance
Sprint Distance
Intensity
Average Heart Rate
Maximum Heart Rate
Sleep Hours
Recovery Score
Goals
Assists
Pass Accuracy
Performance Score

The dataset contains 4,203 session records from 30 athletes covering January 1, 2026 to June 30, 2026.

🔍 Analytics Features

The system calculates:

Daily Workload
Rolling 7-Day Workload
Rolling 28-Day Workload
Personal 28-Day Workload Baseline
Workload Z-Score
Workload Anomaly Flag
Readiness Score
Readiness Status
Readiness Status
Score	Status
80–100	Ready
60–79.99	Moderate
Below 60	Needs Attention
🤖 Machine Learning

The project evaluates machine learning models for predicting the next recorded session's performance score.

Models
Linear Regression — baseline model
XGBoost — advanced model
Improved Linear Regression using historical features
Improved XGBoost using historical features

The project uses a time-based train/test split to reduce temporal leakage.

Model Evaluation
Model	MAE	RMSE	R²
Original Linear Regression	5.275	6.540	-0.006
Original XGBoost	5.572	6.896	-0.119
Improved Linear Regression	5.183	6.516	-0.009
Improved XGBoost	5.439	6.830	-0.109

The results show that historical features slightly reduced prediction error, while the negative R² values indicate that the current synthetic dataset does not support strong predictive performance.

The results are therefore treated as an evaluation finding rather than evidence of a highly accurate prediction system.

🧠 Explainability

Permutation importance is used to understand which features contributed most to the XGBoost model's predictive performance.

The explainability analysis is stored in:

data/xgboost_explainability.csv

Important features observed in the analysis include workload, intensity, heart-rate indicators, sprint distance, and previous performance.

These importance values indicate model association and should not be interpreted as causal relationships.

🖥️ Dashboard

The Streamlit dashboard provides:

Athlete selection
Athlete profile
Readiness score
Readiness status
Recovery score
Coach guidance
Workload trends
Readiness trends
Recovery and sleep trends
Workload anomaly alerts
Recent session history
Athlete summary
ML explainability
FastAPI connection status
🚀 Running the Project
1. Start the FastAPI backend

From the project root:

uvicorn api.app:app --reload

API documentation:

http://127.0.0.1:8000/docs
2. Start the Streamlit dashboard

Open another terminal:

streamlit run dashboard/app.py

The dashboard will open in the browser.

🔌 API Endpoints
Root
GET /
Health Check
GET /health
Athlete Analytics
GET /athletes/{athlete_id}

Example:

GET /athletes/ATH001

The athlete endpoint returns readiness, recovery, performance, workload, workload Z-score, and anomaly information.

🧪 Testing & Validation

The project includes:

Data validation
Missing-value checks
Duplicate checks
Invalid-data detection
API health testing
Athlete endpoint testing
Robustness evidence
Operational monitoring evidence

Testing documentation is available in:

docs/testing_evidence.md
📁 Project Structure
Athlete_Readiness_Project/
│
├── api/
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── athlete_analytics.csv
│   ├── athlete_workload_anomalies.csv
│   ├── football_athlete_sessions_raw.csv
│   ├── football_athlete_sessions_processed.csv
│   └── xgboost_explainability.csv
│
├── docs/
│   ├── deployment_guide.md
│   ├── monitoring_evidence.md
│   ├── system_card.md
│   ├── testing_evidence.md
│   └── user_admin_guide.md
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│   └── data_validation.py
│
├── tests/
│   └── test_data_validation.py
│
├── Dockerfile
├── requirements.txt
└── .gitignore
🛡️ Privacy & Safety

The dataset used in this prototype is synthetic and does not contain real athlete personal or medical records.

Heart-rate, sleep, and recovery values are treated as simulated training indicators and are not intended for medical diagnosis.

📦 Technology Stack
Python
Pandas
NumPy
Scikit-learn
XGBoost
Matplotlib
Seaborn
Streamlit
FastAPI
Uvicorn
Pydantic
Git & GitHub
Docker configuration

👨‍💻 Project

**Athlete Readiness Modeling with Personalized Baselines and Workload Anomaly Detection**

Developed as a T.Y. B.Sc. Data Science capstone project.

Name: Asmit Arvind Shah  
Roll No.: TDDS015B
