
"""Finds the sum of the digits in 2^1000"""
n = str(2 ** 1000)

digit_sum = 0
for d in n:
    digit_sum += int(d)
print(digit_sum)
