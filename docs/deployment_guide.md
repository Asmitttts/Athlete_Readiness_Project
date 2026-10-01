# Deployment Guide

## 1. Project Deployment Structure

The project is organized into separate components:

- `dashboard/` — Streamlit dashboard
- `api/` — FastAPI service
- `data/` — Analytics and dataset files
- `models/` — Machine learning model artifacts
- `src/` — Data validation and supporting source code
- `tests/` — Automated testing
- `logs/` — Operational API logs
- `docs/` — Project documentation

## 2. Local API Deployment

The FastAPI service can be started using:

```bash
uvicorn api.app:app --reload

The API will be available at:

`http://127.0.0.1:8000`

Swagger API documentation is available at:

`http://127.0.0.1:8000/docs`

---

## 3. Local Dashboard Deployment

The Streamlit dashboard can be started using:

```bash
streamlit run dashboard/app.py
```

The dashboard will open in the browser.

---

## 4. Environment Setup

Create and activate the Python virtual environment before running the project.

On Windows:

```bash
py -3.12 -m venv .venv
```

Activate the environment:

```bash
.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```
---

## 5. Docker Deployment

The project includes a `Dockerfile` for containerized API deployment.

Build the Docker image from the project root:

```bash
docker build -t athlete-readiness-api .
```

Run the container:

```bash
docker run -p 8000:8000 athlete-readiness-api
```

The API can then be accessed at:

`http://127.0.0.1:8000`

Swagger documentation:

`http://127.0.0.1:8000/docs`

---

## 6. Deployment Verification

After starting the API, verify the following:

- API root endpoint responds successfully.
- Health endpoint returns `{"status": "healthy"}`.
- Swagger documentation opens successfully.
- Athlete endpoint returns data for a valid athlete ID.
- Invalid athlete IDs return HTTP 404.
- API request logs are generated in `logs/api.log`.

---

## 7. Production Considerations

Before production deployment, the following should be configured:

- Secure authentication and authorization
- HTTPS
- Environment-based configuration
- Secret management
- Input validation
- Dependency and security checks
- Container health checks
- Monitoring and logging
- Backup and recovery procedures
- Protection of athlete data and privacy

---

## 8. Project Startup Order

For local testing, start the services in the following order:

### 1. Activate the virtual environment

```bash
.venv\Scripts\Activate.ps1
```

### 2. Start the FastAPI service

```bash
uvicorn api.app:app --reload
```

### 3. Start the Streamlit dashboard

Open another terminal and run:

```bash
streamlit run dashboard/app.py
```

### 4. Verify the system

Open the dashboard and select an athlete.

Confirm that:

- Athlete information is displayed.
- Readiness information is displayed.
- Workload information is displayed.
- Anomaly information is displayed.
- API connection shows as connected.

---

## 9. Shutdown

To stop a running service, press:

```text
Ctrl + C
```

Stop the API and dashboard terminals separately.

---

## 10. Deployment Status

The project supports local deployment of the FastAPI service and Streamlit dashboard.

Docker deployment configuration is also included through the project `Dockerfile`.

Production deployment requires additional security, authentication, HTTPS, monitoring and infrastructure configuration.


