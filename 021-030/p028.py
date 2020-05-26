"""Number spiral diagonals"""
from time import time
start_time = time()

total = 1
jump = 2
current_num = 1

while jump + 1 <= 1001:
    for i in range(4):
        current_num += jump
        total += current_num
    jump += 2
print(f"{total} found in {time()-start_time} seconds")
