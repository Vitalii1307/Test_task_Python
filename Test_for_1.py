import pytest

def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def test_all_even():
    assert sum_of_even_numbers([2, 4, 6, 8]) == 20

def test_no_even():
    assert sum_of_even_numbers([1, 3, 5, 7]) == 0

def test_mixed():
    assert sum_of_even_numbers([1, 2, 3, 4, 5, 58, 59, 100]) == 164

def test_empty():
    assert sum_of_even_numbers([]) == 0

def test_negative_numbers():
    assert sum_of_even_numbers([-1, -2, -3, -4]) == -6

def test_all_negative_even():
    assert sum_of_even_numbers([-2, -4, -6, -8]) == -20

def test_all_negative_odd():
    assert sum_of_even_numbers([-1, -3, -5, -7]) == 0

if __name__ == '__main__':
    pytest.main([__file__])