import shutil

source = "journal.txt"
destination = "journal_copie.txt"

try:
    shutil.copy(source, destination)
    print(f"Fichier copié de {source} à {destination}.")
except FileNotFoundError:
    print(f"Le fichier source n'a pas été trouvé.")
except IOError:
    print("Erreur lors de la copie du fichier.")