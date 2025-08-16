# Exercise 6: Data analysis with pandas II (10 points)

In this week's exercise we will continue developing our skills using pandas to analyze climate data.

The aim of this exercise is to analyze historical weather data and weather anomalies. In Problem 1 you read in a tricky data file and explore it's contents. In problem 2, you will convert and aggregate the data from daily temperatures in Fahrenheit to monthly average temperatures in Celsius. In Problem 3, you will finally analyze weather anomalies by comparing monthly average temperatures to their long-term average.

## Completing the exercise

- **Exercise 6 is due by the start of the next lesson (9:15 am, October 14th, 2024)**.
- **Remember to save and commit your changes locally, and push your changes to GitHub after each major change**!
- **[Working in pairs](https://geo-python-site.readthedocs.io/en/latest/lessons/L2/why-pairs.html) is optional on this exercise**. If you prefer to work alone, please be sure to inform the course assistants. Otherwise, and we will only grade the repository of the member of your pair that is responsible for this week's exercise.

## Where to find help

- Review the [materials for Lesson 6](https://geo-python-site.readthedocs.io/en/latest/lessons/L6/overview.html)
- Check out the [hints for this week's exercise](https://geo-python-site.readthedocs.io/en/latest/lessons/L6/exercise-6.html#exercise-6-hints) if you're having trouble
- Take a look at the **[PEP 8 - Style guide for Python code](https://www.python.org/dev/peps/pep-0008/)** if you are uncertain about **the style of your code**

## Before you start

### Clone the Exercise 6 repository

Before starting to work with the problems for this week, you should start a new JupyterLab instance and clone your own Exercise 6 repository (e.g., `exercise-6-davewhipp`) in the instance using Git as we saw in [**Lesson 2**](https://geo-python-site.readthedocs.io/en/latest/lessons/L2/git-basics.html#clone-a-repository-from-github).

### Input data

For problems 1-3 in this exercise we will be using historical climate data from the Helsinki-Vantaa airport station.
For these problems, we have daily observations obtained from the [NOAA Global Historical Climatology Network](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND).
The file was downloaded using the "Custom GHCN-Daily Text" output format, including following attributes:

| Attribute                | Description                      |
|--------------------------|----------------------------------|
| `STATION`                | Unique ID of the weather station |
| `ELEVATION`              | Elevation of the station         |
| `LATITUDE` , `LONGITUDE` | Coordinates of the station       |
| `DATE`                   | Date of the measurement          |
| `PRCP`                   | Precipitation                    |
| `TAVG`                   | Average temperature              |
| `TMAX`                   | Maximum temperature              |
| `TMIN`                   | Minimum temperature              |

The file for this problem is exactly as available from the NOAA website. You can take a [look of the data](data/1091402.txt).

**Note**: The temperatures in this dataset are given in degrees Fahrenheit.

Additional information about the data format can be found in the [hints for Exercise 6](https://geo-python-site.readthedocs.io/en/latest/lessons/L6/exercise-6.html#exercise-6-hints).

## Start working

There are three graded problems in this week's exercise and one optional problem.

**Note**: Problems 1-3 are all in one notebook.

1. [Problems 1-3: Analysing Helsinki climate data (10 points)](Exercise-6-problems-1-3.ipynb)
