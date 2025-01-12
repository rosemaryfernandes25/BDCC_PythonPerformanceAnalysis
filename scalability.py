import time
from multiprocessing import Pool
import matplotlib.pyplot as plt
import csv

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range_chunk(chunk):
    """Find primes in a specific range chunk."""
    start, end = chunk
    return [n for n in range(start, end) if is_prime(n)]

def parallel_algorithm(num_workers, start=100000, end=5000000):
    """Run the parallel algorithm with the given number of threads."""
    chunk_size = (end - start) // num_workers

    # Divide the range into chunks
    chunks = [
        (start + i * chunk_size, start + (i + 1) * chunk_size if i != num_workers - 1 else end)
        for i in range(num_workers)
    ]

    start_time = time.time()

    # Parallel computation using Pool
    with Pool(processes=num_workers) as pool:
        results = pool.map(find_primes_in_range_chunk, chunks)

    # Combine results from all chunks
    primes = [prime for chunk in results for prime in chunk]

    end_time = time.time()
    return len(primes), end_time - start_time

def test_scalability():
    # Number of threads to test
    thread_counts = [1, 2, 4, 8, 16]
    execution_times = []
    csv_file = "scalability_results.csv"

    print("Testing scalability with varying threads...")
    
    # Prepare CSV file for writing
    with open(csv_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Number of Threads", "Execution Time (seconds)"])
        
        # Run tests
        for threads in thread_counts:
            print(f"Testing with {threads} threads...")
            _, exec_time = parallel_algorithm(num_workers=threads)
            execution_times.append(exec_time)
            print(f"Execution time: {exec_time:.2f} seconds")
            
            # Write results to CSV
            writer.writerow([threads, f"{exec_time:.3f}"])

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(thread_counts, execution_times, marker='o', linestyle='-', color='b', label='Execution Time')
    plt.title("Scalability of Parallel Algorithm")
    plt.xlabel("Number of Threads")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.xticks(thread_counts)
    plt.tight_layout()
    plt.savefig("scalability_plot.png")  # Save the plot as an image
    plt.show()

if __name__ == "__main__":
    test_scalability()
