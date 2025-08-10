import pandas as pd

# Problem 1

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

# Problem 2

data2 = pd.read_csv(
    "data/6153237444115dat.csv", na_values=["*", "**", "***", "****", "*****", "******"]
)

selected = data2[["USAF", "YR--MODAHRMN", "TEMP", "MAX", "MIN"]].dropna().copy()

selected["Celsius"] = ((selected["TEMP"] - 32) / 1.8).round(0).astype(int)

kumpula_criteria = [29980]
rovaniemi_criteria = [28450]

kumpula = selected.loc[selected["USAF"].isin(kumpula_criteria)]
rovaniemi = selected.loc[selected["USAF"].isin(rovaniemi_criteria)]

kumpula_output = "data/Kumpula_temps_May_Aug_2017.csv"
rovaniemi_output = "data/Rovaniemi_temps_May_Aug_2017.csv"

kumpula.to_csv(kumpula_output, sep=",")
rovaniemi.to_csv(rovaniemi_output, sep=",")

print(kumpula.head())

# problem 3

kumpula = pd.read_csv("data/Kumpula_temps_May_Aug_2017.csv")
rovaniemi = pd.read_csv("data/Rovaniemi_temps_May_Aug_2017.csv")

kumpula_median = kumpula["Celsius"].median()
rovaniemi_median = rovaniemi["Celsius"].median()

kumpula_may = kumpula.loc[
    (kumpula["YR--MODAHRMN"] >= 201705010000)
    & (kumpula["YR--MODAHRMN"] <= 201705312400)
]
rovaniemi_may = rovaniemi.loc[
    (rovaniemi["YR--MODAHRMN"] >= 201705010000)
    & (rovaniemi["YR--MODAHRMN"] <= 201705312400)
]

kumpula_june = kumpula.loc[
    (kumpula["YR--MODAHRMN"] >= 201707010000)
    & (kumpula["YR--MODAHRMN"] <= 201707312400)
]
rovaniemi_june = rovaniemi.loc[
    (rovaniemi["YR--MODAHRMN"] >= 201707010000)
    & (rovaniemi["YR--MODAHRMN"] <= 201707312400)
]
