def sum_square_difference(n):
    numbers = range(1, n + 1)
    sum_squares = sum(i ** 2 for i in numbers)
    square_sum = sum(numbers) ** 2
    return square_sum - sum_squares


print(sum_square_difference(100))
