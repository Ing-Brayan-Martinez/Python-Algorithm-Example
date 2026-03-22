import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from ordering.bubble_sort import bubble_sort
from util.data import get_data, print_data


def test_bubble_sort():
    data = get_data()

    print("\n-- BubbleSort --\n")

    # before
    print("Before Sorting: ")
    print_data(data)

    # sort
    print("\n")
    bubble_sort(data)

    # after
    print("After Sorting: ")
    print_data(data)

    print("\nTest Passed!")


def test_bubble_sort_empty():
    data = []
    bubble_sort(data)
    assert data == []


def test_bubble_sort_single():
    data = [5]
    bubble_sort(data)
    assert data == [5]


def test_bubble_sort_already_sorted():
    data = [1, 2, 3, 4, 5]
    bubble_sort(data)
    assert data == [1, 2, 3, 4, 5]


def test_bubble_sort_unsorted():
    data = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(data)
    assert data == [11, 12, 22, 25, 34, 64, 90]


def test_bubble_sort_reverse():
    data = [5, 4, 3, 2, 1]
    bubble_sort(data)
    assert data == [1, 2, 3, 4, 5]
