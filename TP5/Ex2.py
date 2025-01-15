phrases = [input(f"Entrez la phrase {i + 1} : ") for i in range(3)]

with open("phrases.txt", "w") as fichier:
    for phrase in phrases:
        fichier.write(phrase + "\n")