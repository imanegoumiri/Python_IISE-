with open("phrases.txt", "a") as fichier :
    while True:
        ajouter = input("Voulez-vous ajouter des phrases ?")
        if ajouter == "oui":
            phrase = input("Entrez une phrase : ")
            fichier.write(phrase + "\n")
        else:
            print("Ajout terminé !")
            break