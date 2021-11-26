"""
Lançar as próprias exceções
- https://docs.python.org/3/library/exceptions.html
"""

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erros:
        print(erros)
        raise  # relançar a exceção

try:
    print(divide(2, 0))
except ZeroDivisionError as erros:
    print(erros)
    
def divide2(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser zero")
    return n1 / n2

try:
    print(divide2(2, 0))
except ValueError as erros:
    print(erros)