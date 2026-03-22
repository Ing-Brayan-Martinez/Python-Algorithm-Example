import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from search.binary_search import binary_search


def test_binary_search():
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(binary_search(numbers, 13))  # 6
    print(binary_search(numbers, 8))   # None

    words = ["apple", "banana", "cherry", "date", "kiwi"]
    print(binary_search(words, "cherry"))  # 2
    print(binary_search(words, "mango"))   # None

    print('')
    print('Test Passed!')


def test_binary_search_found():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 10) == 9


def test_binary_search_not_found():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, 11) is None
    assert binary_search(arr, 0) is None


def test_binary_search_empty():
    arr = []
    assert binary_search(arr, 5) is None


def test_binary_search_single_element_found():
    arr = [5]
    assert binary_search(arr, 5) == 0


def test_binary_search_single_element_not_found():
    arr = [5]
    assert binary_search(arr, 3) is None


def test_binary_search_strings():
    arr = ["apple", "banana", "cherry", "date", "elderberry"]
    assert binary_search(arr, "cherry") == 2
    assert binary_search(arr, "apple") == 0
    assert binary_search(arr, "grape") is None
