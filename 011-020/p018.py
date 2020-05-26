
import time
start_time = time.time()

pyramid = []
for line in open('p018.txt').readlines():
    pyramid.append([int(x) for x in line.strip().split()])


for i in range(len(pyramid)):
    try:
        for idx, b in enumerate(pyramid[-(i+2)]):
            pyramid[-(i+2)][idx] += max([pyramid[-(i+1)][idx], pyramid[-(i+1)][idx+1]])
    except IndexError:
        pass

print(f"{pyramid[0][0]} found in {time.time() - start_time} seconds")
