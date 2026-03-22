def fibonacci(n: int) -> int:
    """
    Calcula el n-ésimo número de Fibonacci.

    Args:
        n: Índice del número de Fibonacci a calcular

    Returns:
        El n-ésimo número de Fibonacci
    """
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fibonacci(n - 1) + fibonacci(n - 2)
