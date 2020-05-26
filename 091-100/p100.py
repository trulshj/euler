
b = 15
n = 21
target = int(10e11)

while n < target:
    temp_b = (3 * b) + (2 * n) - 2
    temp_n = (4 * b) + (3 * n) - 3
    b = temp_b
    n = temp_n

print(b)
