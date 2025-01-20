def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erreur : Division par zéro"

print(safe_division(2, 0 ))