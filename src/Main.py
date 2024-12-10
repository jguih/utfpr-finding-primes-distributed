import time;
import random;
from FindPrimes import find_primes_in_interval, find_primes_in_interval_parallel, find_primes_in_interval_distributed

if __name__ == "__main__":
    start = 0
    end = random.randint(10**7, 10**7)
    num_clients = 5  # Number of clients to distribute the task
    print(f"Finding primes between {start} and {end}")

    # Sequencial
    start_time = time.time()
    find_primes_in_interval((start, end))
    print(f"Sequencial time: {(time.time() - start_time) * 1000} ms")

    # Parallel
    start_time = time.time()
    find_primes_in_interval_parallel(start, end)
    print(f"Parallel time: {(time.time() - start_time) * 1000} ms")

    # Distributed
    start_time = time.time()
    find_primes_in_interval_distributed(start, end, num_processes=num_clients)
    print(f"Distributed time: {(time.time() - start_time) * 1000} ms")