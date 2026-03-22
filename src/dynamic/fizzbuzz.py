def fizzbuzz(n: int) -> str:
    """
    Retorna 'FizzBuzz' si n es divisible por 3 y 5,
    'Fizz' si es divisible por 3,
    'Buzz' si es divisible por 5,
    o el número como string en caso contrario.
    
    Args:
        n: Número entero a evaluar
        
    Returns:
        String con el resultado FizzBuzz
    """
    match n:
        case x if x % 3 == 0 and x % 5 == 0:
            return "FizzBuzz"
        case x if x % 3 == 0:
            return "Fizz"
        case x if x % 5 == 0:
            return "Buzz"
        case _:
            return str(n)

