with open("exemple.txt", "r") as fichier:
    lignes = fichier.readlines()
    nbr_lignes = len(lignes)
    nbr_mots = sum(len(ligne.split()) for ligne in lignes)
    nbr_caracteres = sum(len(ligne) for ligne in lignes)

print(f"Nombre total de lignes : {nbr_lignes}")
print(f"Nombre total de mots : {nbr_mots}")
print(f"Nombre total de caractères : {nbr_caracteres}")
