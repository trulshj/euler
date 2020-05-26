
from time import time
start_time = time()

fib_array = [1, 1]


def fibonacci(n):
    if n < 0:
        raise ValueError("Incorrect input")
    elif n <= len(fib_array):
        return fib_array[n-1]
    else:
        temp_fib = fibonacci(n-1) + fibonacci(n-2)
        fib_array.append(temp_fib)
        return temp_fib


idx = 0
while len(str(fibonacci(idx))) < 1000:
    idx += 1

print(f"{idx} found in {round((time()-start_time) * 1000, 3)}ms")
