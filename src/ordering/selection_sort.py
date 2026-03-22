from typing import List


def selection_sort(data: List[int]) -> None:
    """
    Ordena una lista de enteros usando el algoritmo Selection Sort.
    Modifica la lista in-place.

    Args:
        data: Lista de enteros a ordenar
    """
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        if min_index != i:
            _swap(i, min_index, data)


def _swap(first: int, second: int, data: List[int]) -> None:
    """
    Intercambia dos elementos en una lista.

    Args:
        first: Índice del primer elemento
        second: Índice del segundo elemento
        data: Lista donde se realizará el intercambio
    """
    data[first], data[second] = data[second], data[first]
