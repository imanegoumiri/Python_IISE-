def fusionner_dicts(dict1, dict2):
    res = dict1.copy()
    for cle, val in dict2.items():
        if cle in res:
            res[cle] += val
        else:
            res[cle] = val   
    return res
print(fusionner_dicts({'a': 1, 'b': 2}, {'b': 1, 'c': 1}))