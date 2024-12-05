class Animal:
    def faire_du_bruit(self):
        print("Bruit d'animal")
        
class Chien(Animal):
    def faire_du_bruit(self):
        print("Woof !")
c1 = Chien()
c1.faire_du_bruit()

class Chat(Animal):
    def faire_du_bruit(self):
        print("Miaou !")
c2 = Chat()
c2.faire_du_bruit()
