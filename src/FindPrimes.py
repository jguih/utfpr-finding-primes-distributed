from multiprocessing import Pool, cpu_count
from Client import get_primes_from_server

def find_primes_in_interval(start_end):
    """
    Finds all prime numbers in the given interval [start, end].

    :param start_end: Tuple with starting and ending number of interval (inclusive)
    :return: A list of prime numbers within the interval
    """
    start, end = start_end
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            # Check divisors up to the square root of the number
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes


def find_primes_in_interval_parallel(start, end, num_processes = cpu_count()):
    """
    Parallelizes the find_primes_in_interval function using threads.
    
    :param start: The starting number of the interval (inclusive)
    :param end: The ending number of the interval (inclusive)
    :param (optional) num_processes: Number of processes that will be created
    :return: A list of all prime numbers in the interval
    """
    range_size = (end - start + 1) // num_processes
    subranges = [
        (start + i * range_size, (start + i * range_size) + range_size if i < num_processes - 1 else end)
        for i in range(num_processes)
    ]
    
    with Pool(processes=num_processes) as pool:
        results = pool.map(find_primes_in_interval, subranges)

    primes = []
    for sublist in results:
        primes.extend(sublist)

    return sorted(primes)

def find_primes_in_interval_distributed(start, end, num_processes, host='127.0.0.1', port=12345):
    """
    Distributes the find_primes_in_interval function using socket communication.

    :param start: The starting number of the interval (inclusive)
    :param end: The ending number of the interval (inclusive)
    :param num_processes: Number of processes to divide the task among
    :param host: The host address of the server (default is '127.0.0.1')
    :param port: The port number of the server (default is 12345)
    :return: A list of all prime numbers in the interval
    """
    range_size = (end - start + 1) // num_processes
    subranges = [
        (start + i * range_size, (start + (i + 1) * range_size) - 1 if i < num_processes - 1 else end)
        for i in range(num_processes)
    ]
    
    primes = []
    for start, end in subranges:
        primes_from_server = get_primes_from_server(start, end, host, port)
        primes.extend(primes_from_server)

    return sorted(primes)

