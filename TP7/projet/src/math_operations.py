def add(a, b):
    """
    Fonction qui additionne deux nombres.
    
    Args :
    a (float) : Le premier nombre.
    b (float) : Le second nombre.
    
    Returns :
    float : La somme des deux nombres.
    """
    return a + b

def subtract(a, b):
    """
    Fonction qui soustraire deux nombres.
    
    Args :
    a (float) : Le premier nombre.
    b (float) : Le second nombre.
    
    Returns :
    float : La soustraction des deux nombres.
    """
    return a - b

def multiply(a, b):
    """
    Fonction qui multiplie deux nombres.
    
    Args :
    a (float) : Le premier nombre.
    b (float) : Le second nombre.
    
    Returns :
    float : La muliplication des deux nombres.
    """
    return a * b

def divide(a, b):
    """
    Fonction qui divise deux nombres.
    
    Args :
    a (float) : Le premier nombre.
    b (float) : Le second nombre.
    
    Returns :
    float : La division des deux nombres.
    """
    if b == 0:
        raise ValueError("Division par zéro!")
    return a / b