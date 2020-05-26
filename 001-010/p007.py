
"""Find the 10 001st prime number"""

import time
start_time = time.time()


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


primes = 0
n = 0
while primes < 10001:
    n += 1
    if is_prime(n):
        primes += 1

print(f"{n} found in {time.time() - start_time} seconds")
