class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant 

    def retirer(self, montant):
        if self.solde >= montant:
           self.solde -= montant 
        else:
            print("Retrait impossible! ")
   
    def afficher_solde(self):
        return "Le solde actuel : {}".format(self.solde)

cb1 = CompteBancaire("Gi", 10000)
print(cb1.afficher_solde())
cb1.deposer(5000)
print(cb1.afficher_solde())
cb1.retirer(1000)
print(cb1.afficher_solde())
cb1.retirer(20000)
