from typing import List


def get_data() -> List[int]:
    """
    Retorna una lista de enteros de prueba.

    Returns:
        Lista de enteros
    """
    return [6, 2, 26, 12, 1, 5, 8, 14, 10, 17, 32]


def print_data(data: List[int]) -> None:
    """
    Imprime cada elemento de la lista.

    Args:
        data: Lista de enteros a imprimir
    """
    for item in data:
        print(item)
