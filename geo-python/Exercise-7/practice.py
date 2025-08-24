import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import panel as pn

pn.extension()


fp = "data/029740.txt"

data = pd.read_csv(
    fp,
    sep=r"\s+",
    na_values=["*", "**", "***", "****", "*****", "******"],
    usecols=["YR--MODAHRMN", "TEMP", "MAX", "MIN"],
    parse_dates=["YR--MODAHRMN"],
    index_col="YR--MODAHRMN",
)

print(data.head())

oct1_temps = data["TEMP"].loc[data.index >= "201910011200"]

xmin = datetime(2019, 10, 1, 15)
xmax = datetime(2019, 10, 1, 22)

start_time = pd.to_datetime("201910011200")
end_time = pd.to_datetime("201910011500")
cold_time = pd.to_datetime("201910011205")

ax = oct1_temps.plot(
    style="ko--",
    title="Helsinki-Vantaa temperatures",
    xlabel="Date",
    ylabel="Temperature [°F]",
    xlim=[start_time, end_time],
    ylim=[40.0, 46.0],
    label="Observed temperature",
    figsize=(12, 6),
)

ax.legend()

x, y = "201910011800", 42
ax.text(cold_time, 42.0, "<- Coldest temperature in early afternoon")

oct1_afternoon = oct1_temps.loc[oct1_temps.index <= "201910011500"]

ax = oct1_afternoon.plot(
    kind="bar",
    title="Helsinki-Vantaa temperatures",
    xlabel="Date",
    ylabel="Temperature [°F]",
    ylim=[40, 46],
    label="Observed temperature",
    figsize=(12, 6),
)

ax.text(0, 42.1, "Coldest \ntemp \nv")
ax.legend()

# Write figure to PNG file
plt.savefig("bar-plot.png")


july2014_df = data.loc[(data.index >= "201407010000") & (data.index < "201407310000")]

plot = july2014_df.hvplot(
    title="Helsinki-Vantaa temperatures",
    xlabel="Date",
    ylabel="Temperature [°F]",
    ylim=[45.0, 90.0],
)

new_names = {"TEMP": "TEMP_F"}
data = data.rename(columns=new_names)
print(data.head())


print("Number of no-data values per column: ")
print(data.isna().sum())

data.dropna(subset=["TEMP_F"], inplace=True)
print("Number of rows after removing no data values:", len(data))

drpedDataFrame = data.dropna()
print("Number of rows after removin all na values ", len(drpedDataFrame))

data["TEMP_C"] = (data["TEMP_F"] - 32.0) / 1.8

print(data.head())

winter = data.loc[(data.index >= "201212010000") & (data.index < "201303010000")]
winter_temps = winter["TEMP_C"]

spring = data.loc[(data.index >= "201303010000") & (data.index < "201306010000")]
spring_temps = spring["TEMP_C"]

summer = data.loc[(data.index >= "201306010000") & (data.index < "201309010000")]
summer_temps = summer["TEMP_C"]

autumn = data.loc[(data.index >= "201309010000") & (data.index < "201312010000")]
autumn_temps = autumn["TEMP_C"]

plt.clf()
plt.close()

# Winter temps
# plt.figure()
# ax1 = winter_temps.plot(
#     title="Winter Temperatures",
#     ylabel="Temp (°C)"
# )


# # Summer temps
# plt.figure()
# ax2 = summer_temps.plot(
#     title="Summer Temperatures",
#     ylabel="Temp (°C)"
# )

# plt.figure()
# ax3 = spring_temps.plot(
#   title="Spring Temperature",
#   ylabel="Temp (°C)"
# )
# plt.figure()
# ax4 = autumn_temps.plot(
#   title="Autumn Temperature",
#   ylabel="Temp (°C)"
# )
# plt.show()

# Find lower limit for y-axis
min_temp = min(
    winter_temps.min(), spring_temps.min(), summer_temps.min(), autumn_temps.min()
)
min_temp = min_temp - 5.0

# Find upper limit for y-axis
max_temp = max(
    winter_temps.max(), spring_temps.max(), summer_temps.max(), autumn_temps.max()
)
max_temp = max_temp + 5.0

# Print y-axis min, max
print(f"Minimum temperature: {min_temp}")
print(f"Maximum temperature: {max_temp}")


# # Create the figure and subplot axes
# fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# # Define variables to more easily refer to individual axes
# ax11 = axs[0][0]
# ax12 = axs[0][1]
# ax21 = axs[1][0]
# ax22 = axs[1][1]

# # Set plot line width
# line_width = 1.5

# # Plot data
# winter_temps.plot(ax=ax11, c="blue", lw=line_width, ylim=[min_temp, max_temp])
# spring_temps.plot(ax=ax12, c="orange", lw=line_width, ylim=[min_temp, max_temp])
# summer_temps.plot(ax=ax21, c="green", lw=line_width, ylim=[min_temp, max_temp])
# autumn_temps.plot(ax=ax22, c="brown", lw=line_width, ylim=[min_temp, max_temp])

# # Display the plot
# # Note: This is not required, but suppresses text from being printed
# # in the output cell
# plt.show()

# Create the figure and subplot axes
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Define variables to more easily refer to individual axes
ax11 = axs[0][0]
ax12 = axs[0][1]
ax21 = axs[1][0]
ax22 = axs[1][1]

# Set plot line width
line_width = 1.5

# Plot data
winter_temps.plot(
    ax=ax11,
    c="blue",
    lw=line_width,
    ylim=[min_temp, max_temp],
    ylabel="Temperature [°C]",
    grid=True,
)
spring_temps.plot(
    ax=ax12, c="orange", lw=line_width, ylim=[min_temp, max_temp], grid=True
)
summer_temps.plot(
    ax=ax21,
    c="green",
    lw=line_width,
    ylim=[min_temp, max_temp],
    xlabel="Date",
    ylabel="Temperature [°C]",
    grid=True,
)
autumn_temps.plot(
    ax=ax22,
    c="brown",
    lw=line_width,
    ylim=[min_temp, max_temp],
    xlabel="Date",
    grid=True,
)

# Set figure title
fig.suptitle("2012-2013 Seasonal temperature observations" "- Helsinki-Vantaa airport")

# Rotate the x-axis labels so they don't overlap
plt.setp(ax11.xaxis.get_majorticklabels(), rotation=60)
plt.setp(ax12.xaxis.get_majorticklabels(), rotation=20)
plt.setp(ax21.xaxis.get_majorticklabels(), rotation=20)
plt.setp(ax22.xaxis.get_majorticklabels(), rotation=20)

# Season label text
ax11.text(pd.to_datetime("20130215"), -25, "Winter")
ax12.text(pd.to_datetime("20130515"), -25, "Spring")
ax21.text(pd.to_datetime("20130815"), -25, "Summer")
ax22.text(pd.to_datetime("20131115"), -25, "Autumn")

# Display the figure
plt.show()
