# Testing & Robustness Evidence

## 1. Data Quality Testing

The athlete dataset was validated before being used by the system.

| Check | Result |
|---|---:|
| Total Rows | 4,203 |
| Total Columns | 17 |
| Missing Values | 0 |
| Duplicate Records | 0 |
| Invalid Duration Values | 0 |
| Invalid Distance Values | 0 |
| Invalid Intensity Values | 0 |
| Invalid Sleep Values | 0 |
| Invalid Recovery Values | 0 |
| Invalid Dates | 0 |

**Status:** PASS

---

## 2. Invalid Data Detection Test

A test dataset containing invalid values was used to verify that the validation system can detect data-quality problems.

The validation system successfully detected:

- Invalid intensity: 1
- Invalid sleep: 1
- Invalid recovery: 1
- Invalid date: 1

**Status:** PASS — invalid data was successfully detected.

---

## 3. API Health Test

**Endpoint:** `/health`

**Expected:** HTTP 200

**Observed:** HTTP 200

**Response:**
```json
{
  "status": "healthy"
}

## Automated Test Result

The project automated data-validation test was executed using pytest.

**Command:**

```bash
python -m pytest -q

Result:

1 passed

he test successfully verifies that invalid duration, distance, intensity, sleep, recovery, and date values are detected correctly.

### API Health Test

Endpoint: /health

Expected: HTTP 200

Observed: HTTP 200

Response:

{
  "status": "healthy"
}

The API health check successfully confirms that the Athlete Readiness API is running and responding correctly.


