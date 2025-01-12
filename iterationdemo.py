import os
import time
import random

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

# Log timings for each iteration
def test_matrix_multiplication():
    try:
        rows_A, cols_A = 200, 200
        rows_B, cols_B = 200, 200

        print("Generating matrices...")
        matrix_A = generate_matrix(rows_A, cols_A)
        matrix_B = generate_matrix(rows_B, cols_B)

        print("Starting iterations...")
        iterations = 10
        timings = []

        for i in range(iterations):
            print("Iteration %d" % (i + 1))
            start_time = time.time()  # Use time.time() instead of time.perf_counter() in Jython
            matrix_multiply(matrix_A, matrix_B)
            end_time = time.time()
            timings.append(end_time - start_time)

        print("Iterations complete. Writing file...")

        # Save timings to a file
        output_file = "iteration_timings.txt"
        with open(output_file, "w") as f:
            for timing in timings:
                f.write(str(timing) + "\n")

        print("File written successfully to: %s" % output_file)
    except Exception as e:
        print("An error occurred: %s" % str(e))

# Run the function
test_matrix_multiplication()

# Print the working directory
print("Current Working Directory: %s" % os.getcwd())
