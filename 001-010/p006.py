"""Find the difference between the sum of the squares
    and the square of the sum of the first 100 natural numbers"""
square_sum = sum([x ** 2 for x in range(101)])
sum_square = sum(range(101)) ** 2

print(sum_square - square_sum)
