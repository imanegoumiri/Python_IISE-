import csv
import os

class GestionContacts:
    def __init__(self, fichier):
        self.fichier = fichier
        if not os.path.exists(self.fichier):
            print(f"Le fichier {self.fichier} n'existe pas !") 

    def ajouter_contact(self, nom, age, ville):
        with open(self.fichier, "a", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerow([nom, age, ville])
        print(f"Contact ajouté !")

    def afficher_contacts(self):
        with open(self.fichier, "r", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier)
            contacts = list(reader)
            for contact in contacts:
                print(f"Nom : {contact['Nom']}, Age : {contact['Age']}, Ville : {contact['Ville']}")

    def rechercher_contact(self, nom):
        with open(self.fichier, "r", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier)
            for contact in reader:
                if contact['Nom'] == nom:
                    print(f"Contact trouvé : Nom : {contact['Nom']}, Age : {contact['Age']}, Ville : {contact['Ville']}")
                    return
            print("Contact introuvable !")

    def supprimer_contact(self, nom):
        contacts = []
        with open(self.fichier, "r", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier)
            for contact in reader:
                if contact['Nom'] != nom:
                    contacts.append(contact)

        with open(self.fichier, "w", newline="", encoding="utf-8") as fichier:
            fieldnames = ['Nom', 'Age', 'Ville']
            writer = csv.DictWriter(fichier, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)
            print("Contact supprimé !")

def menu():
    gestion = GestionContacts("contacts.csv")

    while True:
        print("\n*** Gestion des Contacts ***")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Entrer un choix : ")
        if choix == "1":
            nom = input("Nom : ")
            age = input("Age : ")
            ville = input("Ville : ")
            gestion.ajouter_contact(nom, age, ville)
        elif choix == "2":
            gestion.afficher_contacts()
        elif choix == "3":
            nom = input("Nom à rechercher : ")
            gestion.rechercher_contact(nom)
        elif choix == "4":
            nom = input("Nom à supprimer : ")
            gestion.supprimer_contact(nom)
        elif choix == "5":
            print("Fin !")
            break
        else:
            print("Entrer un choix entre 1 et 5 !")

if __name__ == "__main__":
    menu()
