from dynamic.factorial import factorial


def test_factorial():
    num = 5
    expected_value = 120

    print('\n-- Factorial --\n')

    result_value = factorial(num)

    print(f'Factorial of {num} is {result_value}\n')

    assert expected_value == result_value

    print('Test Passed!')


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(10) == 3628800
