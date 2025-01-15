import json 

infos = {
    "Nom ": "Gi",
    "Age ": 21,
    "Note ": 18
}

with open('etudiants.json', 'w') as fichier:
    json.dump(infos, fichier, indent=4)

with open('etudiants.json', 'r') as fichier:
    infos = json.load(fichier)
    print(infos)