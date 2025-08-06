# problem 1

# function to convert farenheit to celsius
def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) / 1.8


# problem 2


# function takes temperature in celsius as input and then outputs numbers according to a criteria
def temp_classifier(temp_celsius):
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    elif temp_celsius >= 15:
        return 3


# problem 3 done in problem3.py (importing functions)
