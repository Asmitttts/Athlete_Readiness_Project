# User & Admin Guide

## 1. System Overview

The Athlete Readiness system is designed for coaches and performance analysts to monitor athlete readiness, workload, recovery and workload anomalies.

---

## 2. User Guide — Coach / Performance Analyst

### Step 1: Start the API

Open a terminal in the project root and run:

```bash
uvicorn api.app:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Swagger API documentation is available at:

`http://127.0.0.1:8000/docs`

---

### Step 2: Start the Dashboard

Open another terminal and run:

```bash
streamlit run dashboard/app.py
```

The Athlete Readiness dashboard will open in the browser.

---

### Step 3: Select an Athlete

Use the athlete selection box in the dashboard.

Select an athlete such as:

- ATH001
- ATH002
- ATH003

The dashboard will display athlete-specific information.

---

### Step 4: View Athlete Readiness

The dashboard displays:

- Readiness Score
- Readiness Status
- Recovery Score
- Performance Score
- Workload information
- Workload Z-Score
- Workload anomaly alerts

Readiness status is shown as:

- Ready
- Moderate
- Needs Attention

---

### Step 5: View Workload Trends

The Workload & Readiness Analytics section displays workload trends.

The dashboard shows:

- Rolling 7-Day Workload
- Rolling 28-Day Workload
- Personal 28-Day Baseline
- Workload Z-Score

These indicators help the coach identify unusual workload patterns.

---

### Step 6: View Recovery and Sleep

The dashboard provides recovery and sleep trends.

The coach can review:

- Recovery Score
- Sleep Hours

These indicators are used as part of the readiness analysis.

---

### Step 7: Check Workload Anomalies

The dashboard provides an anomaly alert when an athlete's workload differs significantly from their personalized baseline.

The anomaly information can be reviewed in the anomaly history section.

---

### Step 8: View ML Explainability

The dashboard contains an ML Prediction Explainability section.

It displays feature importance information from the XGBoost model.

This helps the user understand which input features had greater influence on model predictions.

The feature importance values indicate model importance and do not represent causal relationships.

---

## 3. API Usage

The API provides athlete analytics through REST endpoints.

### Health Check

Endpoint:

`GET /health`

Expected response:

```json
{
    "status": "healthy"
}
```

### Athlete Information

Endpoint:

`GET /athletes/{athlete_id}`

Example:

`GET /athletes/ATH001`

The endpoint returns athlete information including:

- Athlete ID
- Age
- Position
- Readiness Score
- Readiness Status
- Recovery Score
- Performance Score
- Rolling 7-Day Workload
- Rolling 28-Day Workload
- Workload Z-Score
- Anomaly Flag

---

## 4. Error Handling

If an athlete ID does not exist, the API returns:

```json
{
    "detail": "Athlete not found"
}
```

with HTTP status code `404`.

---

## 5. Admin Guide

### API Monitoring

API requests are recorded in:

`logs/api.log`

The log records information such as:

- Request method
- Endpoint/path
- HTTP status code
- Request duration
- Timestamp
- Log level

### Data Quality

The system includes data-quality validation checks for:

- Missing values
- Duplicate records
- Invalid duration values
- Invalid distance values
- Invalid intensity values
- Invalid sleep values
- Invalid recovery values
- Invalid dates

The validation script can be executed from the project root using:

```bash
python src/data_validation.py
```

---

## 6. Basic Troubleshooting

### API is not opening

Make sure the API terminal is running:

```bash
uvicorn api.app:app --reload
```

Then open:

`http://127.0.0.1:8000/docs`

### Dashboard is not opening

Make sure the dashboard is running in another terminal:

```bash
streamlit run dashboard/app.py
```

### Dashboard shows API connection error

Check that the FastAPI server is running before starting or using the dashboard.

### Athlete not found

Check that the entered athlete ID exists in the dataset.

Example:

`ATH001`

---

## 7. System Shutdown

To stop the API or dashboard:

1. Open the corresponding terminal.
2. Press `Ctrl + C`.
3. Close the browser tabs if required.

---

## 8. Security and Privacy

The project uses simulated athlete data for development and demonstration.

No real personal or medical information should be entered into the system.

API access should be appropriately secured before production deployment.
