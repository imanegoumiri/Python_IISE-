import pandas as pd

# lire fichier csv
df = pd.read_csv("employes.csv") 

print("Les cinq premières lignes : ")
print(df.head())

# la moyenne de la colonne "Age"
print("Moyenne d'age :", df["Age"].mean())  