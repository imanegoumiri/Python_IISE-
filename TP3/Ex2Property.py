class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

p1 = Personne("ima", "gi", 21)
print(f"Nom : {p1.nom}")
print(f"Prénom : {p1.prenom}")
print(f"Âge : {p1.age}")

p1.nom = "ycb"
p1.prenom = "yz"
p1.age = 27

print("\nAprès modification :")
print(f"Nom : {p1.nom}")
print(f"Prénom : {p1.prenom}")
print(f"Âge : {p1.age}")
