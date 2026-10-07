import matplotlib.pyplot as plt
import numpy as np

# Create 9 graphs
fig, ax = plt.subplots(3, 3, figsize=(15, 12))

# Main Chart Title
fig.suptitle("My First Chart", fontsize=20)

# -------------------------------------------------
# Graph 1 : Pie Chart
# -------------------------------------------------
y = np.array([35, 25, 25, 15])

ax[0, 0].pie(y)
ax[0, 0].set_title("Basic Pie Chart")
ax[0, 0].set_xlabel("Category")
ax[0, 0].set_ylabel("Value")


# -------------------------------------------------
# Graph 2 : Histogram
# -------------------------------------------------
x = np.random.normal(170, 10, 250)

ax[0, 1].hist(x)
ax[0, 1].set_title("Histogram")
ax[0, 1].set_xlabel("Value")
ax[0, 1].set_ylabel("Frequency")


# -------------------------------------------------
# Graph 3 : Bar Chart
# -------------------------------------------------
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

ax[0, 2].bar(x, y)
ax[0, 2].set_title("Bar Chart")
ax[0, 2].set_xlabel("Category")
ax[0, 2].set_ylabel("Value")


# -------------------------------------------------
# Graph 4 : Horizontal Bar Chart
# -------------------------------------------------
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

ax[1, 0].barh(x, y, height=0.1)
ax[1, 0].set_title("Horizontal Bar Chart")
ax[1, 0].set_xlabel("Value")
ax[1, 0].set_ylabel("Category")


# -------------------------------------------------
# Graph 5 : Scatter Plot
# -------------------------------------------------
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

ax[1, 1].scatter(x, y)
ax[1, 1].set_title("Scatter Plot")
ax[1, 1].set_xlabel("X")
ax[1, 1].set_ylabel("Y")


# -------------------------------------------------
# Graph 6 : Colored Scatter Plot
# -------------------------------------------------
x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
sizes = 10 * np.random.randint(100, size=100)

scatter = ax[1, 2].scatter(
    x, y,
    c=colors,
    s=sizes,
    alpha=0.5,
    cmap="nipy_spectral"
)

ax[1, 2].set_title("Colored Scatter Plot")
ax[1, 2].set_xlabel("X")
ax[1, 2].set_ylabel("Y")
fig.colorbar(scatter, ax=ax[1, 2])


# -------------------------------------------------
# Graph 7 : Bubble Scatter Plot
# -------------------------------------------------
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])

ax[2, 0].scatter(x, y, s=sizes, alpha=0.5)
ax[2, 0].set_title("Bubble Scatter Plot")
ax[2, 0].set_xlabel("X")
ax[2, 0].set_ylabel("Y")


# -------------------------------------------------
# Graph 8 : Pie Chart with Labels and Explode
# -------------------------------------------------
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

ax[2, 1].pie(
    y,
    labels=mylabels,
    explode=myexplode
)

ax[2, 1].set_title("Exploded Pie Chart")
ax[2, 1].set_xlabel("Category")
ax[2, 1].set_ylabel("Value")


# -------------------------------------------------
# Graph 9 : Pie Chart with Colors
# -------------------------------------------------
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

ax[2, 2].pie(
    y,
    labels=mylabels,
    colors=mycolors
)

ax[2, 2].set_title("Colored Pie Chart")
ax[2, 2].set_xlabel("Category")
ax[2, 2].set_ylabel("Value")


# Display all graphs
plt.tight_layout()
plt.show()