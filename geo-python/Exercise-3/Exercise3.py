basename = "Station"
print(basename)

filenames = []
print(filenames)

for value in range(21):
    text = f"{basename}_{value}.txt"
    filenames.append(text)

print(filenames)
