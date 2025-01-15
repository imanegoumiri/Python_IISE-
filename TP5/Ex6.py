import os

anc_nom = "phrases.txt"
nouv_nom = "anciennes_phrases.txt"

try:
    os.rename(anc_nom, nouv_nom)
    print(f"Fichier renommé en {nouv_nom}.")
except FileNotFoundError:
    print(f"Le fichier à renommer n'a pas été trouvé.")
except IOError:
    print("Erreur lors du renommage du fichier.")

try:
    os.remove("anciennes_phrases.txt")
    print(f"Fichier {"anciennes_phrases.txt"} supprimé.")
except FileNotFoundError:
    print(f"Le fichier à supprimer n'a pas été trouvé.")
except IOError:
    print("Erreur lors de la suppression du fichier.")
