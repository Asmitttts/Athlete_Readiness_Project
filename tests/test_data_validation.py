import pandas as pd

# Create intentionally invalid test data
test_data = pd.DataFrame({
    "Duration_Min": [-10],
    "Distance_Km": [-5],
    "Intensity_Score": [15],
    "Sleep_Hours": [30],
    "Recovery_Score": [120],
    "Date": ["invalid-date"]
})

# Validation checks
invalid_duration = (test_data["Duration_Min"] <= 0).sum()
invalid_distance = (test_data["Distance_Km"] < 0).sum()
invalid_intensity = (
    (test_data["Intensity_Score"] < 0) |
    (test_data["Intensity_Score"] > 10)
).sum()
invalid_sleep = (
    (test_data["Sleep_Hours"] < 0) |
    (test_data["Sleep_Hours"] > 24)
).sum()
invalid_recovery = (
    (test_data["Recovery_Score"] < 0) |
    (test_data["Recovery_Score"] > 100)
).sum()

test_data["Date"] = pd.to_datetime(
    test_data["Date"],
    errors="coerce"
)

invalid_dates = test_data["Date"].isna().sum()

total_errors = (
    invalid_duration
    + invalid_distance
    + invalid_intensity
    + invalid_sleep
    + invalid_recovery
    + invalid_dates
)

print("===== ROBUSTNESS TEST =====")
print(f"Invalid duration detected: {invalid_duration}")
print(f"Invalid distance detected: {invalid_distance}")
print(f"Invalid intensity detected: {invalid_intensity}")
print(f"Invalid sleep detected: {invalid_sleep}")
print(f"Invalid recovery detected: {invalid_recovery}")
print(f"Invalid dates detected: {invalid_dates}")

if total_errors > 0:
    print("\nPASS - Invalid data was successfully detected.")
else:
    print("\nFAIL - Invalid data was not detected.")