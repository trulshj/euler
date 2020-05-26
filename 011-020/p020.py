
from math import factorial

digit_sum = 0
for n in str(factorial(100)):
    digit_sum += int(n)

print(digit_sum)
