import pandas as pd

# Load raw dataset
df = pd.read_csv("data/football_athlete_sessions_raw.csv")

print("===== DATA QUALITY REPORT =====")

# 1. Dataset shape
print(f"\nRows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# 2. Missing values
missing_values = df.isnull().sum().sum()
print(f"\nMissing values: {missing_values}")

# 3. Duplicate records
duplicates = df.duplicated().sum()
print(f"Duplicate records: {duplicates}")

# 4. Invalid numerical values
invalid_duration = (df["Duration_Min"] <= 0).sum()
invalid_distance = (df["Distance_Km"] < 0).sum()
invalid_intensity = (
    (df["Intensity_Score"] < 0) |
    (df["Intensity_Score"] > 10)
).sum()
invalid_sleep = (
    (df["Sleep_Hours"] < 0) |
    (df["Sleep_Hours"] > 24)
).sum()
invalid_recovery = (
    (df["Recovery_Score"] < 0) |
    (df["Recovery_Score"] > 100)
).sum()

print(f"\nInvalid duration values: {invalid_duration}")
print(f"Invalid distance values: {invalid_distance}")
print(f"Invalid intensity values: {invalid_intensity}")
print(f"Invalid sleep values: {invalid_sleep}")
print(f"Invalid recovery values: {invalid_recovery}")

# 5. Date validation
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
invalid_dates = df["Date"].isna().sum()

print(f"Invalid dates: {invalid_dates}")

# Final status
total_errors = (
    missing_values
    + duplicates
    + invalid_duration
    + invalid_distance
    + invalid_intensity
    + invalid_sleep
    + invalid_recovery
    + invalid_dates
)

print("\n===== FINAL STATUS =====")

if total_errors == 0:
    print("PASS - Data quality checks completed successfully.")
else:
    print(f"FAIL - {total_errors} data quality issues detected.")