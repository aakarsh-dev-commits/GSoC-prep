# Exercise 5: Data analysis with pandas (10 points)

In this exercise, we will be doing data analysis using [pandas - the Python Data Analysis Library](http://pandas.pydata.org/). So far, we have only used example data stored in list variables, and this week we will be loading data files and interacting with actual data sets.

In this exercise you are asked to analyze air temperature data from Kumpula, Helsinki (in Southern Finland) and Rovaniemi (a city in northern Finland) and to explore how their summer temperatures differed in 2017.

## Completing the exercise

- **Exercise 5 is due by the start of the next lesson (9:15 am, October 7th, 2024)**.
- **Remember to save and commit your changes locally, and push your changes to GitHub after each major change**!
- **[Working in pairs](https://geo-python-site.readthedocs.io/en/latest/lessons/L2/why-pairs.html) is optional for this exercise**. **Please inform your course assistant if you and your partner wish to work independently on this exercise**. Otherwise, we will only grade the repository of the member of your pair that is responsible for this week's exercise.

## Where to find help

- Review the [materials for Lesson 5](https://geo-python-site.readthedocs.io/en/latest/lessons/L5/overview.html)
- Check out the [hints for this week's exercise](https://geo-python-site.readthedocs.io/en/latest/lessons/L5/exercise-5.html#exercise-5-hints) if you're having trouble.

## Before you start

### Clone the Exercise 5 repository

Before starting to work with the problems for this week, you should start a new JupyterLab instance and clone your own Exercise 5 repository (e.g., `exercise-5-davewhipp`) in the instance using Git as we saw in [**Lesson 2**](https://geo-python-site.readthedocs.io/en/latest/lessons/L2/git-basics.html#clone-a-repository-from-github).

### Input data

For this exercise we will be using [NOAA weather data](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database). The data has been stored in a CSV file (comma delimited text file) which is stored in this repository: [data/6153237444115dat.csv](data/6153237444115dat.csv).

You can read the full description of the data and all the attributes from this file that is also available in this exercise repository: [data/3505doc.txt](data/3505doc.txt).

The first five rows of the data look like following:

```
USAF,WBAN,YR--MODAHRMN,DIR,SPD,GUS,CLG,SKC,L,M,H,VSB,MW,MW,MW,MW,AW,AW,AW,AW,W,TEMP,DEWP,SLP,ALT,STP,MAX,MIN,PCP01,PCP06,PCP24,PCPXX,SD
028450,99999,201705010000,174,10,14,***,***,*,*,*,2.2,**,**,**,**,67,**,**,**,8,31,31,1009.2,*****,984.1,***,***,*****,*****,*****,*****,35
028450,99999,201705010020,180,10,***,4,***,*,*,*,2.9,**,**,**,**,10,**,**,**,*,30,30,******,29.74,******,***,***,*****,*****,*****,*****,**
028450,99999,201705010050,190,10,***,4,***,*,*,*,2.1,**,**,**,**,10,**,**,**,*,30,30,******,29.74,******,***,***,*****,*****,*****,*****,**
028450,99999,201705010100,188,12,16,***,***,*,*,*,3.2,**,**,**,**,77,**,**,**,*,31,30,1009.1,*****,984.0,***,***,*****,*****,*****,*****,35
```

**NOTICE**: the data includes \* characters that represent NoData values.

The most important attributes for this exercise are:

 - **USAF** = the station ID number
   - 028450 : Rovaniemi
   - 029980 : Helsinki Kumpula
 - **YR--MODAHRMN** = Year-Month-Day-Hour-Minute in Greenwich Mean Time (GMT)
 - **TEMP** = Temperature in Fahrenheit
 - **MAX** = Maximum temperature in Fahrenheit
 - **MIN** = Minimum temperature in Fahrenheit

## Start working

There are three graded problems in this week's exercise and one optional problem.

1. [Problem 1: Basic statistics (2 points)](Exercise-5-problem-1.ipynb)
2. [Problem 2: Data manipulation and subsetting (4 points)](Exercise-5-problem-2.ipynb)
3. [Problem 3: Data analysis (4 points)](Exercise-5-problem-3.ipynb)
4. [Problem 4: Data aggregation (*optional*, 0 points)](Exercise-5-problem-4.ipynb)
