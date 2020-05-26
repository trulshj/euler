
import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    root = math.sqrt(n)
    while i <= root:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


primes = []
for i in range(100000):
    if is_prime(i):
        primes.append(i)


def is_truncatable(n):
    d = len(str(n))
    if d <= 1:
        return False
    n_copy = n
    # Trunc right => left
    for i in range(d):
        n_copy //= 10
        if n_copy not in primes and n_copy > 0:
            return False
    # Trunc left => right
    for i in range(d):
        if n % (10 * (d-i)) in primes:
            continue
        else:
            return False
    return True


ans = 0
num = 0
truncs = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
for p in primes:
    if is_truncatable(p):
        ans += p
        num += 1
print(f"Found {num} truncatable primes with a sum of {ans}")
print(sum(truncs))
