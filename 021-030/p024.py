
import itertools
from time import time
start_time = time()

ans = ""
perm = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[999_999]
for i in perm:
    ans += str(i)
print(f"{ans} found in {time()-start_time} seconds")
