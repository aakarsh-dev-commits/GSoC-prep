import pandas as pd
import random as rd
import matplotlib.pyplot as plt

# problem 1
x = []
y = []

for num in range(1, 1001):
    x.append(rd.random())

for num in range(1, 1001):
    y.append(rd.random())

data = pd.DataFrame(data={"x": x, "y": y})

colors = []
for num in range(1, 1001):
    colors.append(rd.randint(1, 1000))

ax = data.plot(
    kind="scatter",
    x="x",
    y="y",
    s=100,
    c=colors,
    colormap="rainbow",
    edgecolors="black",
    title="My random candy points",
    ylabel="Y-label",
    xlabel="X-label",
)
output = "data/my_first_plot.png"
plt.savefig(output)
plt.show()
