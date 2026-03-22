from typing import List


def bubble_sort(data: List[int]) -> None:
    """
    Ordena una lista de enteros usando el algoritmo Bubble Sort.
    Modifica la lista in-place.
    
    Args:
        data: Lista de enteros a ordenar
    """
    for i in range(len(data) - 1):
        break_count = 0
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                _swap(j, j + 1, data)
                break_count += 1
        if break_count == 0:
            break


def _swap(first: int, second: int, data: List[int]) -> None:
    """
    Intercambia dos elementos en una lista.
    
    Args:
        first: Índice del primer elemento
        second: Índice del segundo elemento
        data: Lista donde se realizará el intercambio
    """
    data[first], data[second] = data[second], data[first]


