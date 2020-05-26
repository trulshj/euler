
from math import sqrt
import time
start_time = time.time()

upper_lim = 10000
a_sum = 0
f_i, f_j = 0, 0


def divisor_sum(n):
    """Returns the number of divisors of a positive integer n"""
    if n <= 1:
        raise ValueError('n must be a positive, non-zero integer')
    root = int(sqrt(n))
    d_sum = 1

    if n == root ** 2:
        d_sum += root
        root -= 1

    for i in range(2, root):
        if n % i == 0:
            d_sum += i + (n/i)

    return d_sum


for i in range(2, upper_lim):
    f_i = divisor_sum(i)
    if i < f_i <= upper_lim:
        f_j = divisor_sum(f_i)
        if f_j == i:
            a_sum += i + f_i

print(f"{int(a_sum)} found in {time.time() - start_time} seconds")
