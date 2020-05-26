
triangle_nums = []


def get_nth_triangle(n):
    return int((n/2) * (n+1))


def is_triangle(n):
    if n in triangle_nums:
        return True
    t = 1
    i = 2
    while t < n:
        t = get_nth_triangle(i)
        if t not in triangle_nums:
            triangle_nums.append(t)
        i += 1


def letter_value(char):
    return ord(char.lower()) - 96


words = [x.strip('\"') for x in open('p042_words.txt').read().split(',')]
triangle_words = 2


for word in words:
    word_sum = 0
    for c in word:
        word_sum += letter_value(c)
    if is_triangle(word_sum):
        triangle_words += 1

print(triangle_words)
