
from time import time
start_time = time()

names = []
for name in open('p022.txt').read().split(','):
    names.append(name.strip('\"'))
names.sort()

total_score = 0
for idx, name in enumerate(names):
    score = 0
    for c in name:
        score += ord(c.lower()) - 96
    total_score += (score * (idx + 1))

print(f"{total_score} found in {time() - start_time} seconds")
