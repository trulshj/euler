
from math import pow
from time import time
start_time = time()


def digit_fifth_power(x):
    if x <= 1:
        return False
    n = 0
    for c in str(x):
        n += pow(int(c), 5)
    if n == x:
        return True
    return False


ans = 0
for i in range(200_000):
    if digit_fifth_power(i):
        ans += i
print(f"{ans} found in {time() - start_time} seconds")
