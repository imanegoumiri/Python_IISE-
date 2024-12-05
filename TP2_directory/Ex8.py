class Personne:
    def __init__(self, nom, prenom, age, list_amis=None):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        if list_amis is None:
            self.list_amis = []
        else:
            self.list_amis = list_amis
    
    def __str__(self):
        return "{} {} agée de {} ans.".format(self.nom, self.prenom, self.age)
    
    def ajouter_ami(self, ami):
        if ami not in self.list_amis:
            self.list_amis.append(ami)

    def afficher_amis(self):
        print("La liste des amis :")
        for ami in self.list_amis:
            print(ami)

p1 = Personne("Gi", "imane", 21)
p2 = Personne("Yz", "yacoub", 28)
p1.ajouter_ami(p2)
p1.afficher_amis()

