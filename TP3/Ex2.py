class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    def getNom(self):
        return self.__nom
    def setNom(self, nom):
        self.__nom = nom

    def getPrenom(self):
        return self.__prenom
    def setPrenom(self, prenom):
        self.__prenom = prenom

    def getAge(self):
        return self.__age 
    def setAge(self, age):
        self.__age = age 

p1 = Personne("ima","gi",21)
print(f"Nom : {p1.getNom()}")
print(f"Prénom : {p1.getPrenom()}")
print(f"Âge : {p1.getAge()}")

p1.setNom("ycb")
p1.setPrenom("yz")
p1.setAge(27)

print("\nAprès modification :")
print(f"Nom : {p1.getNom()}")
print(f"Prénom : {p1.getPrenom()}")
print(f"Âge : {p1.getAge()}")
