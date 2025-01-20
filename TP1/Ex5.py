def factorielle(n):
    f = 0
    if n == 0:
       f = 1
    else:
        f= n * factorielle(n - 1)
    return f
print(factorielle(5))