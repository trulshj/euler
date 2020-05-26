
import time
start_time = time.time()

integer = 0
for line in open("p013.txt").readlines():
    integer += int(line.strip())

print(f"{str(integer)[:10]} found in {time.time() - start_time}")
