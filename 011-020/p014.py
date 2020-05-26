
import time
start_time = time.time()

memo = {1: 1}


def collatz(n):
    """Returns the number of steps required to prove the collatz conjecture for a positive integer n"""
    if n in memo:
        return memo[n]
    if n % 2:
        memo[n] = 2 + collatz((3 * n + 1) / 2)
    else:
        memo[n] = 1 + collatz(n / 2)
    return memo[n]


max_seq = (0, 0)
for i in range(1, 1_000_000):
    current_seq = collatz(i)
    if current_seq > max_seq[0]:
        max_seq = (current_seq, i)

print(f"{max_seq[1]} has a sequence of {max_seq[0]}")
print(f"Found in {time.time() - start_time} seconds")
