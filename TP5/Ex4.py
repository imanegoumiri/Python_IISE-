import csv
with open("contacts.csv", "r", newline='') as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        print(ligne) 