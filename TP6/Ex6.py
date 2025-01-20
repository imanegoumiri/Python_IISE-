def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur : Division par zéro")
    else:
        print(f"La division a été effectué avec succès : {result}")
    finally:
        print("Fin !")
safe_division(10, 2)