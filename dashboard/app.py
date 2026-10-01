import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000"

def get_athlete_from_api(athlete_id):
    try:
        response = requests.get(
            f"{API_URL}/athletes/{athlete_id}",
            timeout=5
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"API connection error: {e}")
        return None
    
st.set_page_config(
    page_title="Athlete Readiness Dashboard",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Athlete Readiness & Workload Dashboard")
st.caption(
    "Coach-focused monitoring of athlete readiness, workload trends, "
    "recovery indicators, and workload anomalies."
)

st.markdown("---")

# Load analytics data
df = pd.read_csv("data/athlete_analytics.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

st.success(f"Analytics data loaded successfully — {len(df):,} records")

st.divider()

# Athlete selection
athletes = sorted(df["Athlete_ID"].unique())

selected_athlete = st.selectbox(
    "Select Athlete",
    athletes
)

api_athlete = get_athlete_from_api(selected_athlete)

if api_athlete:
    st.success("API connection: Connected")

    st.info(
        f"API Readiness: {api_athlete['Readiness_Score']} "
        f"({api_athlete['Readiness_Status']})"
    )
    st.write(
        f"API Workload Z-Score: {api_athlete['Workload_Z_Score']}"
    )

    if api_athlete["Anomaly_Flag"]:
        st.warning("⚠️ API Alert: Workload anomaly detected")
    else:
        st.success("API Alert: No workload anomaly detected")
        
st.write(f"Selected Athlete: **{selected_athlete}**")

# Filter selected athlete
athlete_df = df[df["Athlete_ID"] == selected_athlete].copy()

# Get latest session
latest = athlete_df.sort_values("Date").iloc[-1]

st.divider()

st.subheader("👤 Athlete Profile")

profile_col1, profile_col2, profile_col3 = st.columns(3)

with profile_col1:
    st.metric("Athlete ID", selected_athlete)

with profile_col2:
    st.metric("Age", int(latest["Age"]))

with profile_col3:
    st.metric("Position", latest["Position"])

# Filter selected athlete
athlete_df = df[df["Athlete_ID"] == selected_athlete].copy()

latest = athlete_df.sort_values("Date").iloc[-1]

# Get latest record
latest = athlete_df.sort_values("Date").iloc[-1]

st.divider()

# Readiness section
st.subheader("📊 Athlete Readiness")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Readiness Score",
        f"{latest['Readiness_Score']:.1f}/100"
    )

with col2:
    st.metric(
        "Readiness Status",
        latest["Readiness_Status"]
    )

with col3:
    st.metric(
        "Recovery Score",
        f"{latest['Recovery_Score']:.1f}/100"
    )

    # Coach guidance
if latest["Readiness_Score"] >= 80:
    st.success("🟢 Athlete is currently in the Ready range.")
elif latest["Readiness_Score"] >= 60:
    st.warning("🟡 Athlete is currently in the Moderate readiness range.")
else:
    st.error("🔴 Athlete is currently in the Needs Attention range.")

    st.divider()

st.subheader("📈 Workload Trend")

workload_chart = athlete_df.sort_values("Date").tail(30)

st.line_chart(
    workload_chart.set_index("Date")[
        ["Rolling_7D_Workload", "Rolling_28D_Workload"]
    ]
)

# Performance Trend
st.divider()
st.subheader("🎯 Performance Trend")

performance_chart = athlete_df.sort_values("Date").tail(30)

st.line_chart(
    performance_chart.set_index("Date")[["Performance_Score"]]
)

# ==========================================
# Personal Baseline & Anomaly Detection
# ==========================================

st.divider()
st.subheader("⚠️ Workload Anomaly Monitoring")

latest_baseline = latest["Personal_28D_Baseline"]
latest_workload = latest["Rolling_7D_Workload"]
latest_z = latest["Workload_Z_Score"]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Personal 28D Baseline",
        f"{latest_baseline:.1f}"
    )

with col2:
    st.metric(
        "Current 7D Workload",
        f"{latest_workload:.1f}"
    )

with col3:
    st.metric(
        "Workload Z-Score",
        f"{latest_z:.2f}"
    ) 

if latest["Anomaly_Flag"]:
    st.error(
        "🚨 Workload anomaly detected — "
        "coach should review the athlete's recent workload."
    )
else:
    st.success(
        "✅ Workload is within the athlete's expected range."
    )


# ==========================================
# Recent Session History
# ==========================================

st.divider()
st.subheader("📋 Recent Session History")

display_columns = [
    "Date",
    "Session_Type",
    "Duration_Min",
    "Daily_Workload",
    "Recovery_Score",
    "Performance_Score",
    "Readiness_Score",
    "Readiness_Status",
    "Anomaly_Flag"
]

st.dataframe(
    athlete_df.sort_values("Date", ascending=False)
    .head(10)[display_columns],
    use_container_width=True
)

# ==========================================
# Recovery & Sleep Monitoring
# ==========================================

st.divider()
st.subheader("😴 Recovery & Sleep")

recovery_chart = athlete_df.sort_values("Date").tail(30)

col1, col2 = st.columns(2)

with col1:
    st.write("Recovery Score")
    st.line_chart(
        recovery_chart.set_index("Date")[["Recovery_Score"]]
    )

with col2:
    st.write("Sleep Hours")
    st.line_chart(
        recovery_chart.set_index("Date")[["Sleep_Hours"]]
    )


# ==========================================
# Anomaly History
# ==========================================

st.divider()
st.subheader("🚨 Anomaly History")

anomaly_history = athlete_df[
    athlete_df["Anomaly_Flag"] == True
].sort_values("Date", ascending=False)

if len(anomaly_history) > 0:
    st.warning(
        f"{len(anomaly_history)} workload anomaly session(s) found "
        f"for {selected_athlete}."
    )

    st.dataframe(
        anomaly_history[
            [
                "Date",
                "Rolling_7D_Workload",
                "Personal_28D_Baseline",
                "Workload_Z_Score",
                "Anomaly_Flag"
            ]
        ].head(10),
        use_container_width=True
    )
else:
    st.success("No workload anomalies found for this athlete.")


    # ==========================================
# ML Explainability
# ==========================================

st.divider()
st.subheader("🧠 ML Prediction Explainability")

# Load explainability results
explainability_path = "data/xgboost_explainability.csv"

try:
    explainability_data = pd.read_csv(explainability_path)

    st.write(
        "The chart below shows which features had the greatest influence "
        "on the XGBoost model's predictions."
    )

    # Top 10 features
    top_explainability = explainability_data.head(10).copy()

    st.bar_chart(
        top_explainability.set_index("Feature")["Importance_Mean"]
    )

    st.caption(
        "Higher permutation importance indicates greater influence on "
        "model prediction performance. These values indicate model "
        "importance, not causal relationships."
    )

except FileNotFoundError:
    st.warning(
        "Explainability results are not available yet."
    )


# ==========================================
# Athlete Summary
# ==========================================

st.divider()
st.subheader("📝 Athlete Summary")

avg_readiness = athlete_df["Readiness_Score"].mean()
avg_recovery = athlete_df["Recovery_Score"].mean()
avg_performance = athlete_df["Performance_Score"].mean()
anomaly_count = athlete_df["Anomaly_Flag"].sum()

st.write(
    f"""
    **Athlete:** {selected_athlete}

    **Average Readiness:** {avg_readiness:.1f}/100

    **Average Recovery:** {avg_recovery:.1f}/100

    **Average Performance:** {avg_performance:.1f}/100

    **Total Workload Anomalies:** {anomaly_count}
    """
)

# ==========================================
# Workload & Readiness Analytics
# ==========================================

st.divider()
st.subheader("📊 Workload & Readiness Analytics")

# Workload trend
st.write("### Workload Trend")

workload_chart = athlete_df.sort_values("Date").tail(30)

st.line_chart(
    workload_chart.set_index("Date")[
        ["Rolling_7D_Workload", "Rolling_28D_Workload"]
    ]
)

# Readiness trend
st.write("### Readiness Score Trend")

readiness_chart = athlete_df.sort_values("Date").tail(30)

st.line_chart(
    readiness_chart.set_index("Date")[
        ["Readiness_Score"]
    ]
)

# Recovery and Sleep
st.write("### Recovery & Sleep Trend")

recovery_sleep_chart = athlete_df.sort_values("Date").tail(30)

st.line_chart(
    recovery_sleep_chart.set_index("Date")[
        ["Recovery_Score", "Sleep_Hours"]
    ]
)

