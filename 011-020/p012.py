
"""Highly divisible triangular number"""
import math
import time
start_time = time.time()


def number_of__divisors(n):
    """Returns the number of divisors a number has"""
    root = int(math.sqrt(n))
    divs = 0

    for i in range(1, root+1):
        if n % i == 0:
            divs += 2

    return divs


n = 1
t = 0

while number_of__divisors(t) < 500:
    t += n
    n += 1

print(f"{t} found in {time.time() - start_time} seconds")
