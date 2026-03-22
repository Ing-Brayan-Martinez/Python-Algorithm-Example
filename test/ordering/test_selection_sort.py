import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from ordering.selection_sort import selection_sort
from util.data import get_data, print_data


def test_selection_sort():
    data = get_data()

    print("\n-- SelectionSort --\n")

    # before
    print("Before Sorting: ")
    print_data(data)

    # sort
    print("\n")
    selection_sort(data)

    # after
    print("After Sorting: ")
    print_data(data)

    print("\nTest Passed!")


def test_selection_sort_empty():
    data = []
    selection_sort(data)
    assert data == []


def test_selection_sort_single():
    data = [5]
    selection_sort(data)
    assert data == [5]


def test_selection_sort_already_sorted():
    data = [1, 2, 3, 4, 5]
    selection_sort(data)
    assert data == [1, 2, 3, 4, 5]


def test_selection_sort_unsorted():
    data = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(data)
    assert data == [11, 12, 22, 25, 34, 64, 90]


def test_selection_sort_reverse():
    data = [5, 4, 3, 2, 1]
    selection_sort(data)
    assert data == [1, 2, 3, 4, 5]
