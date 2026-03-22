def factorial(n: int) -> int:
    """
    Calcula el factorial de un número.

    Args:
        n: Número entero no negativo

    Returns:
        El factorial de n
    """
    match n:
        case 0:
            return 1
        case _:
            return n * factorial(n - 1)
