
"""Find the smallest positive integer that is evenly divisible by 1 to 20"""
import time
start_time = time.time()


# Brute force solution
def check_div(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True


num = 0
while True:
    num += 20
    if check_div(num):
        print(f"{num} found in {time.time() - start_time}")
        break
