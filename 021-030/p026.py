
import re

from decimal import *
getcontext().prec = 2
000

max_len = (0, 0)
for i in range(1, 1000):
    string = str(Decimal(1) / Decimal(i))
    repeated = re.findall("(.+?)\\1+", string)
    if len(repeated) >= 1:
        current_len = max([len(x) for x in repeated])
        if current_len > max_len[0]:
            max_len = (current_len, i)
print(max_len[1])
