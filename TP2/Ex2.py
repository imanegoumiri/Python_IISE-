class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        return "Voiture : {} , Modele : {} , Annee : {}".format(self.marque, self.modele, self.annee)
        
v1 = Voiture("bmw","m4",2024)
v2 = Voiture("mercedes","G class",2020)
print(v1.afficher_info())
print(v2.afficher_info())