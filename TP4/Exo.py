class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        return f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}"
    
class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur
    def afficher_moteur(self):
        return f"Puissance: {self.puissance} chevaux, Type de moteur: {self.type_moteur}"

class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places
    def afficher_info(self):
        vehicule_info = Vehicule.afficher_info(self)
        moteur_info = Moteur.afficher_moteur(self)
        return f"{vehicule_info}, Nombre de places: {self.nombre_de_places}, {moteur_info}"

class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto
    def afficher_info(self):
        vehicule_info = Vehicule.afficher_info(self)
        moteur_info = Moteur.afficher_moteur(self)
        return f"{vehicule_info}, Type de moto: {self.type_moto}, {moteur_info}"

v1 = Voiture("bmw", "m4", 2024, 480, "Essence", 4)
m1 = Moto("bmw", "gs", 2020, 125, "Electrique", "Sport")

print(v1.afficher_info())
print(m1.afficher_info())