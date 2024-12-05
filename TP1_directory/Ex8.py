def somme_varargs(*args):
    sum = 0
    for i in args: 
        sum += i
    return sum
print(somme_varargs(2,4))
