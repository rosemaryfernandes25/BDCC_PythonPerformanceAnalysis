import time
import random
import cProfile
import pstats
import csv

# Function to generate a random matrix
def generate_matrix(rows, cols):
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

# Function to multiply two matrices
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Function to benchmark matrix multiplication
def benchmark_matrix_multiply():
    # Matrix sizes for testing
    rows_A, cols_A = 200, 200
    rows_B, cols_B = 200, 200

    # Generate random matrices
    matrix_A = generate_matrix(rows_A, cols_A)
    matrix_B = generate_matrix(rows_B, cols_B)

    # Benchmark the matrix multiplication
    start_time = time.time()
    result_matrix = matrix_multiply(matrix_A, matrix_B)
    end_time = time.time()

    # Display the execution time
    print("Matrix multiplication completed in {:.6f} seconds.".format(end_time - start_time))

# Run cProfile and export results to CSV
if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    benchmark_matrix_multiply()
    pr.disable()

    # Save profiling data to a .prof file
    pr.dump_stats('pypy_matrix.prof')  # This saves the profiling data as a .prof file

    # Save the profiling results in CSV format
    stats = pstats.Stats(pr).sort_stats('tottime')

    # Specify the CSV file name
    csv_file = "pypy_matxresults.csv" #change name according to what is being executed(pypy/python)

    # Write the profiling data to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Function", "Number of Calls", "Total Time (s)", "Per Call Time (s)", "Cumulative Time (s)"])

        for func, stat in stats.stats.items():
            # Handle cases where func has fewer elements
            func_name = f"{func}" if isinstance(func, tuple) else str(func)
            ncalls = stat[0]
            tottime = f"{stat[2]:.3f}"  # Total time formatted to 3 decimals
            percall = f"{stat[2] / ncalls:.3f}" if ncalls > 0 else "0.000"  # Per-call time formatted to 3 decimals
            cumtime = f"{stat[3]:.3f}"  # Cumulative time formatted to 3 decimals
            # Write to CSV
            writer.writerow([func_name, ncalls, tottime, percall, cumtime])

    print(f"Profiling results saved to '{csv_file}'.")
