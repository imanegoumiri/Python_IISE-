class NegativeAgeError(Exception):
    pass
def set_age(age):
    if age < 0:
        raise NegativeAgeError("L'age ne peut pas etre négatif !")
try:
    set_age(-2)
except NegativeAgeError as e:
    print(e)