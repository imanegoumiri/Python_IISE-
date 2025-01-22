import os
from datetime import datetime
import math

rep = os.listdir('.') 
print("Repertoire courant :", rep)

maintenant = datetime.now()
print("Date et heure :", maintenant)

nbr = float(input("Entrer un nombre :"))
racine = math.sqrt(nbr)
print(f"Racine carré : {racine : .2f}")