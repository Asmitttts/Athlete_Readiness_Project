from fastapi import FastAPI, HTTPException, Request
import pandas as pd
import logging
import time
import os

# ==========================================
# Operational Logging
# ==========================================

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/api.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("athlete_readiness_api")


app = FastAPI(
    title="Athlete Readiness API",
    description="API for athlete readiness, workload and performance analytics",
    version="1.0.0"
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = round(time.time() - start_time, 4)

    logger.info(
        f"{request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Duration: {duration}s"
    )

    return response


@app.get("/")
def root():
    return {
        "message": "Athlete Readiness API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/athletes/{athlete_id}")
def get_athlete(athlete_id: str):
    df = pd.read_csv("data/athlete_analytics.csv")

    athlete_df = df[df["Athlete_ID"] == athlete_id]

    if athlete_df.empty:
        raise HTTPException(
            status_code=404,
            detail="Athlete not found"
        )

    latest = athlete_df.sort_values("Date").iloc[-1]

    return {
        "Athlete_ID": latest["Athlete_ID"],
        "Age": int(latest["Age"]),
        "Position": latest["Position"],
        "Date": latest["Date"],
        "Readiness_Score": round(float(latest["Readiness_Score"]), 2),
        "Readiness_Status": latest["Readiness_Status"],
        "Recovery_Score": round(float(latest["Recovery_Score"]), 2),
        "Performance_Score": round(float(latest["Performance_Score"]), 2),
        "Rolling_7D_Workload": round(float(latest["Rolling_7D_Workload"]), 2),
        "Rolling_28D_Workload": round(float(latest["Rolling_28D_Workload"]), 2),
        "Workload_Z_Score": round(float(latest["Workload_Z_Score"]), 2),
        "Anomaly_Flag": bool(latest["Anomaly_Flag"])
    }