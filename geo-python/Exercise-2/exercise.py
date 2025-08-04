# Problem 0

stationName = [
    "lighthouse",
    "Harmaja",
    "Suomenlinna aaltopoiju",
    "Kumpula",
    "Kaisaniemi",
]
yearOperation = [2003, 1989, 2016, 2005, 1844]

print(stationName)
print(yearOperation)


stationName.append("Alajärvi Möksy")
yearOperation.append(1957)

print(stationName)
print(yearOperation)

stationName.append("Alajärvi Möksy")
yearOperation.append(1957)

print(stationName)
print(yearOperation)


stationName.sort()
yearOperation.sort()

print(stationName)
print(yearOperation)

yearOperation.sort()

print(stationName)
print(yearOperation)

# Problem 1

temp = [-3.5, -4.0, -1.0, 4.0, 10.0, 14.5, 17.5, 16.0, 11.5, 6.0, 2.0, -1.5]
month = [
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

index = input("Enter month index Eg Jan is 0 ")

infoText = (
    f"The average temperature in Helsinki in {month[int(index)]} is {temp[int(index)]}"
)

print(infoText)
