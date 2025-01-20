class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def se_presenter(self):
        return "Je m'appelle {} {} et j'ai {} ans.".format(self.nom, self.prenom, self.age)

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
    def etudier(self):
        return "L'étudiant qui a le matricule {} étudie.".format(self.matricule)

p1 = Personne("Gi", "imane", 21)
print(p1.se_presenter())

e1 = Etudiant("Yz", "yacoub", 28, "JT0011")
print(e1.se_presenter())
print(e1.etudier())
