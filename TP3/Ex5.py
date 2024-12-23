class Empolye:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    def __str__(self):
        return f"{self.nom} {self.prenom}, Salaire: {self.salaire}"

class Manager(Empolye):
    def __init__(self, nom, prenom, salaire, list_emp = None):
        super().__init__(nom, prenom, salaire)
        if list_emp is None:
            self.list_emp = []
        else: 
            self.list_emp = list_emp
    
    def ajouter_emp(self, emp):
        if emp not in self.list_emp:
            self.list_emp.append(emp)

    def afficher_emp(self):
        print("Liste des employés :")
        for emp in self.list_emp:
            print(emp)

e1 = Empolye("julan", "sami", 10000)
e2 = Empolye("yzid", "yassu", 15000)
manager = Manager("yacoub", "yz", 20000,[e1,e2])
e3 = Empolye("gi", "imane", 10000)
manager.ajouter_emp(e3)
manager.afficher_emp()