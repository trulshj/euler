
import functools as ft
import time
start_time = time.time()


grid = []
for line in open("p011.txt").readlines():
    grid.append([int(x) for x in line.strip().split(" ")])

max_prod = 0

# Horizontal
for row in grid:
    for i in range(len(row) - 3):
        current_prod = ft.reduce(lambda a, b: a * b, row[i: i+4])
        if current_prod > max_prod:
            max_prod = current_prod

# Vertical
for col in range(len(grid[0])):
    for i in range(len(grid[0]) - 3):
        current_prod = ft.reduce(lambda a, b: a * b, [item[col] for item in grid[i:i+4]])
        if current_prod > max_prod:
            max_prod = current_prod

# Diagonal left => right
for j in range(17):
    for i in range(17):
        current_prod = grid[i-j][i] * grid[i-j+1][i+1] * grid[i-j+2][i+2] * grid[i-j+3][i+3]
        if current_prod > max_prod:
            max_prod = current_prod

# Diagonal right => left
for j in range(3, 20):
    for i in range(3, 20):
        current_prod = grid[i-j][i] * grid[i-j+1][i-1] * grid[i-j+2][i-2] * grid[i-j+3][i-3]
        if current_prod > max_prod:
            max_prod = current_prod

print(max_prod, "found in", time.time() - start_time, "seconds")
