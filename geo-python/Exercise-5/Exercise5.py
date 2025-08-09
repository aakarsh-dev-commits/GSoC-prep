import pandas as pd

data = pd.read_csv(
    "data/6153237444115dat.csv", na_values=["*", "**", "***", "****", "*****", "******"]
)

print(data.head())

rows_count = len(data)

column_names = data.columns.values


column_datatype = data.dtypes

print(column_names)
print(column_datatype)

input = "data/6153237444115dat.csv"

temp_mean = data["TEMP"].mean()

print(temp_mean)

temp_max_std = data["MAX"].std()

station_count = data["USAF"].count()
