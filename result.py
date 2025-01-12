import json
import matplotlib.pyplot as plt

# Load the benchmark data from the JSON file
with open('benchmark_data.json', 'r') as f:
    data = json.load(f)

# Extract the benchmark times
benchmark_times = [entry['stats']['mean'] for entry in data['benchmarks']]

# Plotting the benchmark times
plt.plot(benchmark_times)
plt.title('Matrix Multiplication Benchmark')
plt.xlabel('Test Run')
plt.ylabel('Mean Time (seconds)')
plt.grid(True)
plt.show()
