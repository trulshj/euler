
from time import time
start_time = time()

upper_lim = 1_000_000


def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


ans = 0
for i in range(1, upper_lim):
    if is_palindrome(i):
        if is_palindrome(bin(i)[2:]):
            ans += i
print(f"{ans} found in {time() - start_time} seconds")
