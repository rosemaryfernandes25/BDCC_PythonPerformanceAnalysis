import matplotlib.pyplot as plt

# Read timings from the txt file
timings = []
with open("iteration_timings.txt", "r") as file:
    for line in file:
        timings.append(float(line.strip()))

# Plot the timings
plt.plot(range(1, len(timings) + 1), timings, marker='o')
plt.title("Matrix Multiplication Timing per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
