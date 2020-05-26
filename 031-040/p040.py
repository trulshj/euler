
constant = ""
n = 1
ans = 1

while len(constant) <= 1000000:
    constant += str(n)
    n += 1

ans *= int(constant[0])
ans *= int(constant[9])
ans *= int(constant[99])
ans *= int(constant[999])
ans *= int(constant[9_999])
ans *= int(constant[99_999])
ans *= int(constant[999_999])

print(ans)
