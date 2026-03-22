
from dynamic.fibonacci import fibonacci


def test_fibonacci():
    num = 20
    expected_value = 6765

    print('\n-- Fibonacci --\n')

    result_value = fibonacci(num)

    print(f'Fibonacci of {num} is {result_value}\n')

    assert expected_value == result_value

    print('Test Passed!')


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_sequence():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, exp in enumerate(expected):
        assert fibonacci(i) == exp
