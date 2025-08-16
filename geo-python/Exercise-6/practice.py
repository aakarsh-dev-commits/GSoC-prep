import pandas as pd

path = "data/1091402.txt"
rovaniemi_path = "data/Rovaniemi_station.csv .csv"

data = pd.read_csv(path, na_values=["-"])
data2 = pd.read_csv(rovaniemi_path, na_values=["-"])

print(data.columns.values)
print(data.columns)
print("data 2 is")
print(data2.head())


data3 = pd.read_csv(
    rovaniemi_path, usecols=["Observation station", "Year", "Month", "Day"]
)

print("data 3 is")
print(data3.head())

newNames = {
    "Observation station": "STATION",
    "Time [Local time]": "TIME",
    "Air temperature mean [°C]": "TEMP_C",
}

data2 = data2.rename(columns=newNames)
print(data2.head())


def celsius_to_fahr(temp_celsius):
    converted_temp = (temp_celsius * 1.8) + 32
    return converted_temp


data2["TEMP_F"] = 0.0

for idx, row in data2.iterrows():
    temp_fahr = celsius_to_fahr(row["TEMP_C"])
    data2.at[idx, "TEMP_F"] = temp_fahr

print(data2.head())

print(data2["Month"].head(10))

data2["MONTH_STR"] = data2["Month"].astype(str)
data2["DAY_STR"] = data2["Day"].astype(str)

data2["MONTH_DAY"] = (
    data2["MONTH_STR"].str.zfill(2) + "-" + data2["DAY_STR"].str.zfill(2)
)

print(data2.head())

data2["YEAR_STR"] = data2["Year"].astype(str)

data2["DATE_STR"] = (
    data2["YEAR_STR"] + data2["MONTH_STR"].str.zfill(2) + data2["DAY_STR"].str.zfill(2)
)

print(data2.head())

data2["DATE"] = pd.to_datetime(data2["DATE_STR"])
print(data2["DATE"].head(10))

data2["MONTH_DAY_DT"] = data2["DATE"].dt.strftime("%m-%d")

print(data2["MONTH_DAY_DT"].head(10))

print(data2.head())

grouped = data2.groupby("MONTH_DAY")
print(f"len of grp is {len(grouped)}")
print(f"len of grp is {data2["MONTH_DAY"].nunique()}")

print(f"grp is {grouped.groups.keys()}")

day = "07-07"

grp1 = grouped.get_group(day)

print(grp1)
print(data2["MONTH_DAY"])
print(data2.head(10))

mean_values = grp1[["TEMP_C", "TEMP_F"]].mean()

print(mean_values)

for key, group in grouped:
    print(f"Key:\n {key}")
    print(f"\nFirst rows of data in this group:\n {group.head()}")
    break

daily_data = pd.DataFrame()

mean_cols = ["TEMP_F", "TEMP_C"]

for key, group in grouped:
    mean_values = group[mean_cols].mean()
    mean_values["MONTH_DAY"] = key
    row = mean_values.to_frame().transpose()
    daily_data = pd.concat([daily_data, row], ignore_index=True)

print(daily_data)
