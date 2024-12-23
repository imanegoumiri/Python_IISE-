from Ex4 import Produit
class Commande:
    def __init__(self, produit, quantite):
        if isinstance(produit, Produit):
            self.produit = produit
            self.quantite = quantite
        else:
            raise ValueError("produit est instance de Produit")

class Panier: 
    def __init__(self, list_cmd=None):
        if list_cmd is None:
            self.list_cmd = []
        else:
            self.list_cmd = list_cmd
    
    def ajouter_commande(self, cmd):
        if cmd not in self.list_cmd:
            self.list_cmd.append(cmd)

    def calculer_total(self, remise = 0):
        total = 0
        for cmd in self.list_cmd:
            total += cmd.produit.calculer_prix(remise) * cmd.quantite
        return total

p1 = Produit("veste", 1500)
p2 = Produit("chemise", 900)
c1 = Commande(p1, 2)
c2 = Commande(p2, 1)
panier = Panier([c1])
panier.ajouter_commande(c2)
print(f"Total du panier : {panier.calculer_total(0.2)}")

