import cProfile
import pstats
import csv
import time

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    return [n for n in range(start, end) if is_prime(n)]

def without_parallelism():
    start, end = 100000, 5000000  # Define a large range
    start_time = time.time()
    
    primes = find_primes_in_range(start, end)
    
    end_time = time.time()
    print(f"Found {len(primes)} primes.")
    print(f"Time taken without parallelism: {end_time - start_time:.2f} seconds")

def profile_and_save_to_csv():
    # Profile the function
    profile_file = "without_parallelism.prof"
    csv_file = "without_parallelism.csv"
    
    print("Profiling the script...")
    cProfile.run("without_parallelism()", profile_file)

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
