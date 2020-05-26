
from math import factorial
import time
start_time = time.time()


def lattice(m, n):
    return int(factorial(m + n) / (factorial(m) * factorial(n)))


print(f"{lattice(2, 3)} found in {time.time() - start_time} seconds")
