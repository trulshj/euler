
from time import time
start_time = time()


def area(x1, y1, x2, y2, x3, y3):
    """Returns the area of a triangle with given coordinates"""
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def contains_origin(x1, y1, x2, y2, x3, y3):
    """Determines whether a triangle with given coordinates contains the origin of a cartesian plane"""
    a = area(x1, y1, x2, y2, x3, y3)
    a1 = area(0, 0, x2, y2, x3, y3)
    a2 = area(x1, y1, 0, 0, x3, y3)
    a3 = area(x1, y1, x2, y2, 0, 0)
    if a == a1 + a2 + a3:
        return True
    else:
        return False


# Parse the input
triangles = []
f = open('p102_triangles.txt').readlines()
for line in f:
    triangles.append([int(x) for x in line.split(',')])

# Count the number of triangles that contain the origin
ans = 0
for t in triangles:
    if contains_origin(t[0], t[1], t[2], t[3], t[4], t[5]):
        ans += 1
print(f"{ans} found in {time() - start_time} seconds")
