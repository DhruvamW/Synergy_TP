import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def prepare_supervised_data(df):
    df = df.dropna(subset=["crop_disease_status"]).copy()

    """
    Excluded features:
    farm_id
    sensor_id
    harvest_date
    total_days
    yield_kg_per_hectare
    timestamp
    """

    features = [
        "crop_type",
        "soil_moisture_%",
        "soil_pH",
        "temperature_C",
        "rainfall_mm",
        "humidity_%",
        "sunlight_hours",
        "irrigation_type",
        "fertilizer_type",
        "pesticide_usage_ml",
        "sowing_date",
        "NDVI_index",
        "latitude",
        "longitude"
    ]

    X = df[features]
    y = df["crop_disease_status"]

    return X, y