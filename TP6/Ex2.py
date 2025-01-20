def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "Erreur : La converstion a échoué"

print(convert_to_int("Gi"))