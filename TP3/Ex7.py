from abc import ABC, abstractmethod
class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass
    
class Voiture(Vehicule):
    def deplacer(self):
        return "la voiture sur la route"
class Bicyclette(Vehicule):
    def deplacer(self):
        return "la bicyclette sur la piste"

v1 = Voiture()
print(v1.deplacer())
b1 = Bicyclette()
print(b1.deplacer())