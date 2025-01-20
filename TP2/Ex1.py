class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age 
    def aboyer(self):
        print("Woof!")

c1 = Chien("Gost","Berger",4)
c1.aboyer()