import time
from multiprocessing import Pool
import cProfile
import pstats
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

def with_parallelism():
    start, end = 100000, 5000000  # Define a large range
    num_workers = 4  # Number of parallel processes
    chunk_size = (end - start) // num_workers

    # Divide the range into chunks, ensuring the last chunk covers all remaining numbers
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
    print(f"Found {len(primes)} primes.")
    print(f"Time taken with parallelism: {end_time - start_time:.2f} seconds")

def profile_and_save_to_csv():
    # Profile the function
    profile_file = "with_parallelism.prof"
    csv_file = "with_parallelism.csv"

    print("Profiling the script...")
    cProfile.run("with_parallelism()", profile_file)

    # Convert the profiling results to CSV
    print("Converting profiling results to CSV...")
    with open(csv_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Function (File:Line:Name)", "Calls", "Time per Call (s)", "Total Time (s)"])
        
        # Load and process profiling stats
        stats = pstats.Stats(profile_file)
        stats.strip_dirs()
        stats.sort_stats("cumulative")
        
        for func, (cc, nc, tt, ct, callers) in stats.stats.items():
            # Dynamic function details
            func_details = f"{func[0]}:{func[1]}:{func[2]}"  # File:Line:Function
            writer.writerow([
                func_details,  # Function details
                nc,  # Number of calls
                f"{(tt / nc):.3f}" if nc > 0 else "0.000",  # Time per call (rounded to 3 decimals)
                f"{ct:.3f}"  # Total time (rounded to 3 decimals)
            ])
    
    print(f"Profiling results saved to {csv_file}")

if __name__ == "__main__":
    profile_and_save_to_csv()
