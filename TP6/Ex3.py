def read_file(filename):
    try:
        with open(filename, "r") as fichier:
            contenu = fichier.read()
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé !")
    else:
        print("Contenu du fichier :")
        print(contenu)
    finally:
        print("Fin !")

read_file("exemple.txt")
