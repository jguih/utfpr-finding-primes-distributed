def find_primes_in_interval(start, end):
    """
    Finds all prime numbers in the given interval [start, end].

    :param start: The starting number of the interval (inclusive)
    :param end: The ending number of the interval (inclusive)
    :return: A list of prime numbers within the interval
    """
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


# Example usage:
start = 0
end = 1000
primes = find_primes_in_interval(start, end)
print(f"Prime numbers between {start} and {end}: {primes}")
