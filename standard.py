import time  # Importation du module time pour utiliser la fonction sleep()

# Définition de la fonction de téléchargement de fichier
def telecharger_fichier(nom, duree):
    print(f"Début du téléchargement de {nom}...")  # Affiche le début du téléchargement
    time.sleep(duree)  # Simule un délai pour le téléchargement du fichier (attend pendant 'duree' secondes)
    print(f"{nom} téléchargé!")  # Affiche que le fichier a été téléchargé

# Téléchargement séquentiel de deux fichiers
telecharger_fichier("Fichier1", 3)  # Télécharge "Fichier1" pendant 3 secondes
telecharger_fichier("Fichier2", 2)  # Télécharge "Fichier2" pendant 2 secondes