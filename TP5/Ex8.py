try:
    with open("inexistant.txt", "r") as fichier:
        print(fichier.read())
except FileNotFoundError:
    print(f"Le fichier 'inexistant.txt' n'a pas été trouvé.")  