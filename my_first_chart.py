import matplotlib.pyplot as plt
import numpy as np

# =========================
# Data
# =========================
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 3, 7, 4])

# =========================
# Create 9 Graphs
# =========================
fig, ax = plt.subplots(3, 3, figsize=(15, 12))

# ชื่อ Chart หลัก
fig.suptitle("My First Chart", fontsize=20)

# =========================
# Graph 1 : Scatter Plot
# =========================
ax[0, 0].scatter(x, y)
ax[0, 0].set_title("Scatter Plot")
ax[0, 0].set_xlabel("X")
ax[0, 0].set_ylabel("Y")

# =========================
# Graph 2 : Colored Scatter
# =========================
colors = ["red", "blue", "green", "orange", "purple"]
ax[0, 1].scatter(x, y, c=colors)
ax[0, 1].set_title("Colored Scatter Plot")
ax[0, 1].set_xlabel("X")
ax[0, 1].set_ylabel("Y")

# =========================
# Graph 3 : Horizontal Bar
# =========================
name = ["A", "B", "C", "D", "E"]
value = [10, 25, 15, 30, 20]

ax[0, 2].barh(name, value)
ax[0, 2].set_title("Horizontal Bar Chart")
ax[0, 2].set_xlabel("Value")
ax[0, 2].set_ylabel("Category")

# =========================
# Graph 4 : Line Chart
# =========================
ax[1, 0].plot(x, y, marker="o")
ax[1, 0].set_title("Line Chart")
ax[1, 0].set_xlabel("X")
ax[1, 0].set_ylabel("Y")
ax[1, 0].grid(True)

# =========================
# Graph 5 : Diamond Line
# =========================
x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([5, 2, 6, 1, 7])

ax[1, 1].plot(x2, y2, marker="D")
ax[1, 1].set_title("Diamond Line Chart")
ax[1, 1].set_xlabel("X")
ax[1, 1].set_ylabel("Y")
ax[1, 1].grid(True)

# =========================
# Graph 6 : Line Chart
# =========================
y3 = np.array([2, 6, 3, 8, 10])

ax[1, 2].plot(x, y3, marker="o")
ax[1, 2].set_title("Line Graph")
ax[1, 2].set_xlabel("X")
ax[1, 2].set_ylabel("Y")
ax[1, 2].grid(True)

# =========================
# Graph 7 : Histogram
# =========================
data = np.random.normal(50, 10, 100)

ax[2, 0].hist(data, bins=10)
ax[2, 0].set_title("Histogram")
ax[2, 0].set_xlabel("Value")
ax[2, 0].set_ylabel("Frequency")

# =========================
# Graph 8 : Pie Chart
# =========================
sizes = [25, 30, 20, 25]
labels = ["A", "B", "C", "D"]

ax[2, 1].pie(sizes, labels=labels, autopct="%1.1f%%")
ax[2, 1].set_title("Pie Chart")
ax[2, 1].set_xlabel("Category")
ax[2, 1].set_ylabel("Value")

# =========================
# Graph 9 : Pie Chart
# =========================
sizes2 = [35, 25, 15, 25]
labels2 = ["A", "B", "C", "D"]

ax[2, 2].pie(sizes2, labels=labels2, autopct="%1.1f%%")
ax[2, 2].set_title("Pie Chart 2")
ax[2, 2].set_xlabel("Category")
ax[2, 2].set_ylabel("Value")

# =========================
# Show Chart
# =========================
plt.tight_layout()
plt.show()