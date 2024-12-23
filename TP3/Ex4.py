class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix):
        self.__prix = prix 

    def calculer_prix(self, remise):
        if self.prix > 1000:
            return self.prix * (1 - remise) 
        return self.prix

p1 = Produit("veste", 1500)
print(f"Prix actuel : {p1.calculer_prix(0.2)}")