import pandas as pd

data = pd.read_csv("data/1091402.txt", skiprows=[1], na_values=[-9999], sep=r"\s+")
data.columns = data.columns.str.strip()

tavg_nodata_count = data["TAVG"].isna().sum()
tmin_nodata_count = data["TMIN"].isna().sum()

print(tavg_nodata_count)
print(tmin_nodata_count)

data = data.dropna()

print(data.tail())

day_count = data["DATE"].nunique()
first_obs = data["DATE"][0]
last_obs = data["DATE"].iloc[-1]
print(day_count)
print(first_obs)
print(last_obs)

avg_temp = data["TAVG"].mean()

print(avg_temp)

summer_1969 = data.loc[(data["DATE"] >= 19690501) & (data["DATE"] <= 19690831)]

print(summer_1969.head())

avg_temp_1969 = summer_1969["TMAX"].mean()
print(avg_temp_1969)

data["DATE"] = data["DATE"].astype(str)
data["DATE_DT"] = pd.to_datetime(data["DATE"])
print(data["DATE_DT"].head(10))
print(data.tail(10))

data["YR-MO"] = data["DATE_DT"].dt.strftime("%Y-%m")

print(data.tail(10))

grouped = data.groupby(data["YR-MO"])

print(grouped.groups.keys())

mean_cols = ["TAVG", "TMAX", "TMIN"]
monthly_data = pd.DataFrame()
for key, group in grouped:
    mean_values = group[mean_cols].mean()
    mean_values["YR-MO"] = key
    row = mean_values.to_frame().transpose()
    monthly_data = pd.concat([monthly_data, row], ignore_index=True)

print(monthly_data)

monthly_data["temp_celsius"] = (monthly_data["TAVG"] - 32) * 5 / 9

print(monthly_data)
