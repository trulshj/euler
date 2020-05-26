"""Find a pythagorean triplet where a + b + c equals 1000"""

from math import sqrt
import time
start_time = time.time()

for a in range(500):
    for b in range(1, a):
        c = sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print(f"{a * b * c} found in {time.time() - start_time} seconds")
            exit()
