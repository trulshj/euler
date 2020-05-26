"""Find the sum of all the primes below 2 000 000"""

import time
start_time = time.time()


def is_prime(n):
    # 1 is not a prime
    if n <= 1:
        return False
    # If n is 2 or 3, it's prime
    if n <= 3:
        return True
    # Check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    # Only check up to the square root of the number
    while i ** 2 <= n:
        # Now we can check 6k +- 1
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


total = 5

for i in range(0, 2_000_000, 6):
    if is_prime(i+1):
        total += i
    if is_prime(i-1):
        total += i

print(f"{total} found in {time.time() - start_time} seconds")
