# Athlete Readiness Modeling — System Card

## 1. System Overview

**Project Title:** Athlete Readiness Modeling with Personalized Baselines and Workload Anomaly Detection

**Sport:** Football / Soccer

**Primary User:** Coach / Performance Analyst

The system analyzes athlete training workload, recovery indicators and performance data to provide athlete-specific readiness information and workload anomaly alerts.

The system includes:

- Athlete profiles
- Workload calculations
- Rolling workload features
- Personalized workload baselines
- Workload anomaly detection
- Readiness scoring
- Performance analysis
- Machine learning experiments
- Interactive Streamlit dashboard
- FastAPI service
- Data-quality validation
- API monitoring and logging

---

## 2. Data

The project uses a safely simulated football athlete-session dataset.

Each record represents an athlete training session.

Main data fields include:

- Athlete ID
- Age
- Position
- Date
- Session type
- Session duration
- Distance
- Sprint distance
- Intensity score
- Average heart rate
- Maximum heart rate
- Sleep hours
- Recovery score
- Goals
- Assists
- Pass accuracy
- Performance score

The dataset contains 4,203 session records from 30 simulated athletes.

---

## 3. Analytics

The system derives:

- Daily workload
- Rolling 7-day workload
- Rolling 28-day workload
- Personal 28-day workload baseline
- Workload Z-score
- Workload anomaly flag
- Readiness score
- Readiness status

The workload anomaly system compares recent workload with an athlete-specific historical baseline.

Anomaly detection uses an absolute Z-score threshold greater than 2.

---

## 4. Readiness Model

The readiness score combines:

- Recovery score
- Recent performance
- Sleep
- Workload status

The resulting score is scaled between 0 and 100.

Readiness categories are:

- 80–100: Ready
- 60–79.99: Moderate
- Below 60: Needs Attention

The readiness score is an analytical indicator and is not a medical diagnosis.

---

## 5. Machine Learning

The project evaluates machine learning for predicting the next recorded session's Performance Score.

Two model families were compared:

- Linear Regression
- XGBoost

A time-based evaluation approach was used.

History-based features were also tested, including:

- Previous performance
- Recent average performance
- Recent average recovery
- Recent average workload

The improved Linear Regression model achieved:

- MAE: 5.182543
- RMSE: 6.516448
- R²: -0.009465

The improved XGBoost model achieved:

- MAE: 5.439491
- RMSE: 6.830412
- R²: -0.109081

The results indicate that the current simulated dataset does not provide strong predictive performance. The ML component is therefore treated as an experimental modelling component rather than a production-grade prediction system.

---

## 6. Explainability

Permutation importance was used to examine feature influence on the XGBoost model.

The explainability analysis provides model-level feature importance information.

Important features observed in the experiment included:

- Average heart rate
- Maximum heart rate
- Intensity score
- Daily workload
- Sprint distance
- Previous performance

These results describe model behaviour and should not be interpreted as causal relationships.

---

## 7. Dashboard

The Streamlit dashboard provides:

- Athlete selection
- Athlete profile
- Readiness score
- Recovery information
- Coach guidance
- Workload trend
- Readiness trend
- Recovery and sleep trend
- Personal workload baseline
- Workload Z-score
- Anomaly alerts
- Recent session history
- ML explainability

---

## 8. API

The FastAPI service provides:

- `/`
- `/health`
- `/athletes/{athlete_id}`

The athlete endpoint returns the latest available analytical information for the requested athlete.

Invalid athlete IDs return HTTP 404.

The API provides automatically generated OpenAPI/Swagger documentation.

---

## 9. Data Quality

Data validation checks include:

- Missing values
- Duplicate records
- Invalid duration
- Invalid distance
- Invalid intensity
- Invalid sleep
- Invalid recovery
- Invalid dates

The current dataset passed the main data-quality checks with zero detected errors.

Additional testing confirmed that intentionally invalid values can be detected.

---

## 10. Monitoring and Audit

The API records operational information in:

`logs/api.log`

Logged information includes:

- Request method
- Request path
- HTTP status code
- Request duration
- Timestamp
- Log level

The `/health` endpoint provides a basic service-health check.

---

## 11. Privacy and Safety

The project uses simulated athlete data rather than real personal athlete records.

Heart-rate, sleep and recovery fields are treated as simulated training indicators.

The system should not be used as:

- A medical diagnostic system
- A clinical decision-making system
- A replacement for professional medical advice

Coach decisions should consider additional real-world context that may not be represented in the dataset.

---

## 12. Known Limitations

The current prototype has several limitations:

1. The dataset is simulated.
2. The machine-learning models currently show weak predictive performance.
3. The current API primarily serves calculated analytics rather than performing live model inference.
4. Athlete readiness depends on the quality and completeness of input data.
5. Workload anomaly thresholds may require domain-specific calibration.
6. The system has not been clinically validated.
7. Real-world deployment would require stronger security, authentication, authorization and privacy controls.

---

## 13. Intended Use

The prototype is intended to demonstrate how athlete workload, recovery and performance information can be combined into an operational analytics workflow for coaches and performance analysts.

It is designed as a decision-support prototype rather than an autonomous decision-making system.

---

## 14. System Status

**Prototype Status:** Functional industry-style prototype

**Dashboard:** Implemented

**FastAPI:** Implemented and tested

**Data validation:** Implemented and tested

**Operational logging:** Implemented and tested

**Machine learning:** Evaluated experimentally

**Explainability:** Implemented

**Container configuration:** Prepared

**Production deployment:** Not claimed