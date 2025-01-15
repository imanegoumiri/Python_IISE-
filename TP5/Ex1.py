with open("exemple.txt", "r") as fichier:
    n = 1
    lignes = fichier.readlines()
    for ligne in lignes:
        print("Ligne ", n, ":", ligne)
        n += 1