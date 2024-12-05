class Livre:
    def __init__(self, titre, auteur, annee_pub):
        self.titre = titre
        self.auteur = auteur
        self.annee_pub = annee_pub
    def __str__(self):
        return "{} de l'auteur {} publié en {}.".format(self.titre, self.auteur, self.annee_pub)

class Bibliotheque:
    def __init__(self, list_liv=None):
        if list_liv is None:
            self.list_liv = []
        else:
            self.list_liv = list_liv
    
    def ajouter_livre(self, liv):
        if liv not in self.list_liv:
            self.list_liv.append(liv)

    def afficher_livres(self):
        print("La liste des livres :")
        for liv in self.list_liv:
            print(liv)

l1 = Livre("Voyage", "Louis", 1932)
l2 = Livre("Guerre", "Léon", 1865)
biblio = Bibliotheque([l1,l2])
l3 = Livre("L'étranger", "Albert Camus", 1942)
biblio.ajouter_livre(l3)
biblio.afficher_livres()