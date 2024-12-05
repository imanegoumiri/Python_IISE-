def analyse_texte(texte):
    nbr_mots = 0
    nbr_caracteres = len(texte)
    mot = False
    for caractere in texte: 
        if caractere != ' ':
            if not mot:
                nbr_mots += 1
                mot = True
        else:
            mot = False
    return {
        "nombre de mots": nbr_mots,
        "nombre de caracteres": nbr_caracteres
    }
print(analyse_texte("Bonjour imane"))  
