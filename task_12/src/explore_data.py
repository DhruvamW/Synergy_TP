import pandas as pd

df = pd.read_csv(r"Synergy_TP\task_12\data\Smart_Farming_Crop_Yield_2024.csv")

print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.isnull().sum().sum()) #tells us where the missing data is.
print(df["crop_disease_status"].value_counts(dropna=False)) #gives the counts
print(df["crop_disease_status"].value_counts(normalize=True, dropna=False)) #gives the proportions

print("Unique farms:", df["farm_id"].nunique())
print("Unique sensors:", df["sensor_id"].nunique())
print("Unique regions:", df["region"].nunique())
print("Unique crops:", df["crop_type"].nunique())

print(df["region"].value_counts())
print(df["crop_type"].value_counts())

df["timestamp"] = pd.to_datetime(df["timestamp"])
print("Start:", df["timestamp"].min())
print("End:", df["timestamp"].max())
print("Unique dates:", df["timestamp"].nunique())
print(df["timestamp"].dt.month.value_counts().sort_index())
print(
    df.groupby(
        df["timestamp"].dt.month,
        dropna=False
    )["crop_disease_status"]
    .value_counts()
)

print(
    pd.crosstab(
        df["region"],
        df["crop_disease_status"],
        margins=True
    )
)
