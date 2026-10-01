# Operational Monitoring & Audit Evidence

## 1. API Request Logging

The Athlete Readiness API implements operational request logging using Python logging and FastAPI middleware.

The log file is stored at:

`logs/api.log`

The logging system records:

- Request method
- Request endpoint/path
- HTTP status code
- Request duration
- Timestamp
- Log level

## 2. Health Monitoring

The API provides a health-check endpoint:

`GET /health`

Successful response:

```json
{
  "status": "healthy"
}