import pandas as pd


def test_invalid_data_detection():
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

    # Verify that every invalid value was detected
    assert invalid_duration > 0
    assert invalid_distance > 0
    assert invalid_intensity > 0
    assert invalid_sleep > 0
    assert invalid_recovery > 0
    assert invalid_dates > 0