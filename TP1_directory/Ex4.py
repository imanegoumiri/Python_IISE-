def compte_occurences(liste):
    occ = {}
    for mot in liste:
        if mot in occ:
            occ[mot] += 1
        else:
            occ[mot] = 1
    return occ
print(compte_occurences(["ali", "anna", "anna"]))