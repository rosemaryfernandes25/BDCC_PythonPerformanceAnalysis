#Using pytest-benchmark
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

# Benchmarking the matrix multiplication
def test_matrix_multiplication(benchmark):
    # Matrix sizes for testing
    rows_A, cols_A = 200, 200
    rows_B, cols_B = 200, 200

    # Generate random matrices
    matrix_A = generate_matrix(rows_A, cols_A)
    matrix_B = generate_matrix(rows_B, cols_B)

    # Benchmark the matrix multiplication function
    result = benchmark(matrix_multiply, matrix_A, matrix_B)

    # Optionally, validate the result's dimensions
    assert len(result) == rows_A and len(result[0]) == cols_B
