import pandas as pd

data = pd.read_csv("data/1091402.txt", skiprows=[1], na_values=[-9999], sep=r"\s+")
data.columns = data.columns.str.strip()

# path = "data/output.csv"

# data.to_csv(path,sep=",")

# print(data.head())

tavg_nodata_count = 0

tavg_nodata_count = data["TAVG"].isna().sum()
tmin_nodata_count = data["TMIN"].isna().sum()

# print(tavg_nodata_count)
# print(tmin_nodata_count)

day_count = data["DATE"].nunique()
first_obs = data["DATE"][0]
last_obs = data.loc[23715, "DATE"]
print(day_count)
print(first_obs)
print(last_obs)

avg_temp = data["TAVG"].mean()

print(avg_temp)

summer_1969 = data.loc[(data["DATE"] >= 19690501) & (data["DATE"] <= 19690831)]

# print(summer_1969.head())

avg_temp_1969 = summer_1969["TMAX"].mean()
print(avg_temp_1969)
