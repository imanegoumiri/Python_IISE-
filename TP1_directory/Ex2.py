def max_tuple(t):
    max = t[0]
    for i in t:
        if i > max:
            max = i 
    return max
print(max_tuple((1,5,3)))