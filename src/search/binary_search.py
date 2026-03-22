from typing import List, TypeVar, Optional

T = TypeVar("T")


def binary_search(arr: List[T], objective: T) -> Optional[int]:
    """
    Busca un elemento en una lista ordenada usando búsqueda binaria.

    Args:
        arr: Lista ordenada de elementos comparables
        objective: Elemento a buscar

    Returns:
        Índice del elemento si se encuentra, None en caso contrario
    """
    left = 0
    right = len(arr)

    while left < right:
        mid = left + (right - left) // 2

        comparison = _compare(arr[mid], objective)

        if comparison == 0:
            return mid
        if comparison < 0:
            left = mid + 1
        else:
            right = mid

    return None


def _compare(value: T, other: T) -> int:
    """
    Compara dos valores del mismo tipo.

    Args:
        value: Primer valor a comparar
        other: Segundo valor a comparar

    Returns:
        Negativo si value < other, 0 si son iguales, positivo si value > other
    """
    if isinstance(value, (int, float, str)):
        if value < other:
            return -1
        if value > other:
            return 1
        return 0
    # Para otros tipos que implementen comparación
    if value < other:
        return -1
    if value > other:
        return 1
    return 0
