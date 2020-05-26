
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def is_pandigital(a, b, c):
    n = str(a) + str(b) + str(c)
    if sorted(n) == digits:
        return True
    return False


ans = 0
for a in range(1, 100):
    for b in range(1, 1000):
        c = a * b
        if is_pandigital(a, b, c):
            ans += c
print(ans)
