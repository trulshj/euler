"""find the largest palindrome number that is a product of two three-digit numbers"""
import time
start_time = time.time()


def is_palindrome(x):
    """Determines if a number 'x' is a palindrome"""
    x = str(x)
    if x[::-1] == x:
        return True
    return False


highest = 0
for i in range(900, 1000):
    for j in range(900, 1000):
        if is_palindrome(i*j):
            if highest < i*j:
                highest = i*j

print(f"{highest} found in {round(time.time() - start_time, 7)} seconds")
