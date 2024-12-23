from Ex1 import Cercle, Rectangle 

def afficher_surface(formes):
    for forme in formes:
        print(f"Surface de la forme : {forme.calculer_surface():.2f}")

c1 = Cercle(5)
r1 = Rectangle(2, 2)
formes = [c1, r1]
afficher_surface(formes)
