ice_cream_rating = 6
sleeping_rating = 9

print(ice_cream_rating)
print(sleeping_rating)

first_name = "Aakarsh"
last_name = "Srivastava"
my_name = first_name + " " + last_name

print(first_name)
print(last_name)
print(my_name)

happiness_rating = (ice_cream_rating + sleeping_rating) / 2
print(happiness_rating)

print(type(ice_cream_rating))
print(type(sleeping_rating))
print(type(happiness_rating))


print(
    "My name is",
    first_name,
    "and I give eating ice cream a score of",
    ice_cream_rating,
    "out of 10! I am",
    my_name,
    "and my sleeping enjoyment rating is",
    sleeping_rating,
    "/ 10! Based on the factors above, my happiness rating is",
    happiness_rating,
    "out of 10, or",
    float(happiness_rating * 10),
    "%!",
)
