def get_positive_integer():
    while True:
        try:
            value = int(input("Saisir un entier positif : "))
            if value <= 0:
                print("Erreur : L'entier doit être positif")
            else:
                print(f"L'entier est :{value}")
                break
        except ValueError:
            print("Erreur : L'entier invalide")
    
get_positive_integer()