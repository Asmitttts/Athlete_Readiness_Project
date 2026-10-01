# Evaluation Dossier

## 1. Evaluation Overview

The Athlete Readiness Modeling system was evaluated across data quality,
workload anomaly detection, readiness scoring, machine learning performance,
explainability, API functionality, and automated testing.

The evaluation uses the project's synthetic football athlete session dataset
containing 4,203 session records from 30 athletes.

---

## 2. Data Quality Evaluation

The raw dataset was validated using an automated data-quality validation
script.

### Results

- Records: 4,203
- Columns: 17
- Missing values: 0
- Duplicate records: 0
- Invalid duration values: 0
- Invalid distance values: 0
- Invalid intensity values: 0
- Invalid sleep values: 0
- Invalid recovery values: 0
- Invalid date values: 0

### Outcome

All implemented data-quality checks passed successfully.

---

## 3. Workload Anomaly Detection Evaluation

Workload anomalies were detected using a personalized baseline approach.

The system calculates:

- Rolling 7-day workload
- Rolling 28-day workload
- Personal 28-day workload baseline
- Workload Z-score

A session is flagged as an anomaly when the absolute workload Z-score
exceeds the defined threshold.

The improved anomaly detection approach produced an anomaly rate of
approximately 7.52% across the dataset.

This approach reduced excessive anomaly flagging compared with the initial
fixed percentage-deviation rule.

---

## 4. Readiness Evaluation

The readiness score combines:

- Recovery score
- Recent performance
- Sleep
- Workload status

The resulting readiness score is mapped into three categories:

- Ready
- Moderate
- Needs Attention

The dashboard displays the latest readiness score and status for the
selected athlete.

---

## 5. Machine Learning Evaluation

The project evaluated Linear Regression as a simpler baseline and XGBoost
as the advanced model.

The target variable is the performance score of the athlete's next
recorded session.

### Original Feature Set

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 5.274561 | 6.540188 | -0.006186 |
| XGBoost | 5.571794 | 6.896373 | -0.118766 |

### Improved Feature Set

Historical features were added, including:

- Previous Performance
- Recent Average Performance
- Recent Average Recovery
- Recent Average Workload

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Improved Linear Regression | 5.182543 | 6.516448 | -0.009465 |
| Improved XGBoost | 5.439491 | 6.830412 | -0.109081 |

### Interpretation

Adding historical features produced a small improvement in MAE and RMSE
for both evaluated models.

However, the R² values remained slightly negative. Therefore, the current
models should be treated as an experimental predictive component rather
than a highly accurate performance prediction system.

The results are reported without hiding the weaker model performance.

---

## 6. Model Explainability

Permutation importance was used to examine which features influenced the
XGBoost model's predictive performance.

The highest observed importance values included:

1. Avg_Heart_Rate
2. Max_Heart_Rate
3. Intensity_Score
4. Daily_Workload
5. Sprint_Distance_Km
6. Previous_Performance

These results describe model feature importance and should not be
interpreted as causal relationships.

---

## 7. API Evaluation

The FastAPI service was tested using the health endpoint.

### Health Check

- Endpoint: `GET /health`
- Expected status: HTTP 200
- Observed status: HTTP 200
- Response: `{"status": "healthy"}`

The athlete endpoint was also tested using valid athlete IDs and returned
athlete-specific readiness and workload information.

Invalid athlete IDs correctly return HTTP 404 with an
`Athlete not found` response.

---

## 8. Automated Testing

The project includes an automated data-validation test using pytest.

### Result

```text
1 passed

The test verifies that invalid duration, distance, intensity, sleep,
recovery, and date values are detected correctly.

9. Limitations

The dataset used for development is synthetic and does not represent
clinical or medical measurements.

The current machine learning results show limited predictive strength,
particularly based on the negative R² values.

The system should therefore be used as a prototype decision-support tool
for workload and readiness analysis rather than as a replacement for
professional coaching or medical judgement.

10. Overall Evaluation

The prototype successfully demonstrates an end-to-end workflow covering
data validation, personalized workload analysis, anomaly detection,
readiness scoring, machine learning experimentation, explainability,
dashboard visualization, API access, monitoring, and automated testing.

The evaluation results and limitations are documented to support further
development and stakeholder testing.