import math


def divisor_sum(num):
    if num == 1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while divisor < n:
        if num % divisor == 0:
            total += divisor
            total += num // divisor
        divisor += 1
    if n ** 2 == num:
        total += n
    return total


def is_abundant(num):
    if divisor_sum(num) > num:
        return True
    else:
        return False


abundant_nums = []
for x in range(0, 28124):
    if is_abundant(x):
        abundant_nums.append(x)
del abundant_nums[0]

sums = [0] * 28124
for x in range(0, len(abundant_nums)):
    for y in range(x, len(abundant_nums)):
        current_sum = abundant_nums[x] + abundant_nums[y]
        if current_sum <= 28123:
            if sums[current_sum] == 0:
                sums[current_sum] = current_sum

t = 0
for x in range(1, len(sums)):
    if sums[x] == 0:
        t += x

print(t)
