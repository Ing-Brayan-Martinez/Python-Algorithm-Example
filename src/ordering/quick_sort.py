from typing import List


def quick_sort(data: List[int]) -> None:
    """
    Ordena una lista de enteros usando el algoritmo Quick Sort.
    Modifica la lista in-place.
    
    Args:
        data: Lista de enteros a ordenar
    """
    lower = 0
    upper = len(data) - 1

    if upper > lower:
        partition_index = _partition(data, lower, upper)

        _internal_quick_sort(data, lower, partition_index - 1)
        _internal_quick_sort(data, partition_index + 1, upper)


def _partition(data: List[int], lower: int, upper: int) -> int:
    """
    Particiona la lista usando el último elemento como pivote.
    
    Args:
        data: Lista a particionar
        lower: Índice inferior
        upper: Índice superior
        
    Returns:
        Índice de la posición final del pivote
    """
    i = lower - 1
    pivot = data[upper]

    for j in range(lower, upper):
        if data[j] <= pivot:
            i += 1
            _swap(i, j, data)

    _swap(i + 1, upper, data)
    return i + 1


def _internal_quick_sort(data: List[int], lower: int, upper: int) -> None:
    """
    Función recursiva interna para ordenar sub-listas.
    
    Args:
        data: Lista a ordenar
        lower: Índice inferior
        upper: Índice superior
    """
    if upper > lower:
        partition_index = _partition(data, lower, upper)

        _internal_quick_sort(data, lower, partition_index - 1)
        _internal_quick_sort(data, partition_index + 1, upper)


def _swap(first: int, second: int, data: List[int]) -> None:
    """
    Intercambia dos elementos en una lista.
    
    Args:
        first: Índice del primer elemento
        second: Índice del segundo elemento
        data: Lista donde se realizará el intercambio
    """
    data[first], data[second] = data[second], data[first]
