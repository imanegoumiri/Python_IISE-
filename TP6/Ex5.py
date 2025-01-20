def process_input(user_input):
    try:
        value = int(user_input)
        result = 10 / value
    except ValueError:
        print("Erreur : Ce n'est pas un nombre valide.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro.")
    else:
        print(f"Le résultat est {result}.")
    finally:
        print("Fin !")

process_input("gi")