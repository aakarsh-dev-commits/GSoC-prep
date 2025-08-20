import pandas as pd

# Read weather data, skip header row with dashes, convert -9999 to NaN
data = pd.read_csv("data/1091402.txt", skiprows=[1], na_values=[-9999], sep=r"\s+")
data.columns = data.columns.str.strip()

# Count missing values in temperature columns
tavg_nodata_count = data["TAVG"].isna().sum()
tmin_nodata_count = data["TMIN"].isna().sum()

print(tavg_nodata_count)
print(tmin_nodata_count)

# Remove rows with any missing data
data = data.dropna()

print(data.tail())

# Basic statistics from the data
day_count = data["DATE"].nunique()
first_obs = data["DATE"][0]
last_obs = data["DATE"].iloc[-1]
print(day_count)
print(first_obs)
print(last_obs)

avg_temp = data["TAVG"].mean()

print(avg_temp)

# Filter for Summer of '69 (May-August 1969)
summer_1969 = data.loc[(data["DATE"] >= 19690501) & (data["DATE"] <= 19690831)]

print(summer_1969.head())

avg_temp_1969 = summer_1969["TMAX"].mean()
print(avg_temp_1969)

# Convert dates and create monthly groupings
data["DATE-STR"] = data["DATE"].astype(str)
data["DATE_DT"] = pd.to_datetime(data["DATE-STR"])
print(data["DATE_DT"].head(10))
print(data.tail(10))

data["YR-MO"] = data["DATE_DT"].dt.strftime("%Y-%m")

print(data.tail(10))

grouped = data.groupby(data["YR-MO"])

print(grouped.groups.keys())

# Calculate monthly averages
mean_cols = ["TAVG", "TMAX", "TMIN"]
monthly_data = pd.DataFrame()
for key, group in grouped:
    mean_values = group[mean_cols].mean()
    mean_values["YR-MO"] = key
    row = mean_values.to_frame().transpose()
    monthly_data = pd.concat([monthly_data, row], ignore_index=True)

print(monthly_data)

# Convert Fahrenheit to Celsius
monthly_data["temp_celsius"] = (monthly_data["TAVG"] - 32) * 5 / 9

print(monthly_data)

# Problem 3

period = data.loc[(data["DATE"] >= 19520101) & (data["DATE"] <= 19801231)].copy()

period["month"] = period["YR-MO"].str.split("-").str[1]

period["month"] = period["month"].astype(int)
print(f"this is period \n {period.head()}")
grouping = period.groupby(period["month"])

print(grouping.groups.keys())

reference_temps = pd.DataFrame()

for key, group in grouping:
    avg_values = group[["TAVG"]].mean()
    avg_values["month"] = key
    row = avg_values.to_frame().transpose()
    reference_temps = pd.concat([reference_temps, row], ignore_index=True)


newcols = {"TAVG": "ref_temp"}
reference_temps = reference_temps.rename(columns=newcols)

reference_temps["ref_temp"] = (reference_temps["ref_temp"] - 32) * 5 / 9

print(reference_temps.head(13))


monthly_data["month"] = monthly_data["YR-MO"].str.split("-").str[1]
monthly_data["month"] = monthly_data["month"].astype(int)


print(monthly_data.head(20))
print(reference_temps.head(20))

join1 = monthly_data.merge(reference_temps, on="month")
join1["diff"] = join1["temp_celsius"] - join1["ref_temp"]

print(join1.head(24))
