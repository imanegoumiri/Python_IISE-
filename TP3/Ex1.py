from abc import ABC, abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        raise NotImplementedError("Not implemented!")

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def calculer_surface(self):
        return math.pi*(self.rayon)**2 

class Rectangle(Forme):
    def __init__(self, larg, haut):
        self.larg = larg    
        self.haut = haut 
    def calculer_surface(self):
        return self.larg*self.haut
