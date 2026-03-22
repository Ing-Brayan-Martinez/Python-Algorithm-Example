import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from dynamic.fizzbuzz import fizzbuzz


def test_fizzbuzz():
    num = 60
    expected_value = "FizzBuzz"

    print("\n-- FizzBuzz --\n")

    result_value = fizzbuzz(num)

    print(f"FizzBuzz of {num} is {result_value}\n")

    assert expected_value == result_value

    print("\nTest Passed!")


def test_fizzbuzz_divisible_by_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"


def test_fizzbuzz_divisible_by_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"


def test_fizzbuzz_divisible_by_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"


def test_fizzbuzz_not_divisible():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"
