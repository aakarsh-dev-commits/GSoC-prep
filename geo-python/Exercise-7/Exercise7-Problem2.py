import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/helsinki-vantaa.csv")
print(data.head())

data["DATE"] = pd.to_datetime(data["DATE"])
data = data.set_index("DATE")
print(data.head())

data = data.sort_index()

selection = data.loc["1988-01-01":"2018-12-01"]

plt.figure()

ax = selection["TEMP_C"].plot(
    figsize=(14, 6),
    style="ko-",
    title="Helsinki-Vantaa Airport",
    ylabel="Temperature (Celsius)",
    xlabel="Time",
)

output = "data/temp_line_plot.png"

plt.savefig(output)
plt.show()
