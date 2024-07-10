def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)


numbers = [1, 2, 3, 4, 5, 58, 59, 100]
print(sum_of_even_numbers(numbers))
