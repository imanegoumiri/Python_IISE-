import unittest

def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division par zéro.")
    return a / b
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("Converstion à échoué.")
def read_file(filename):
    try:
        with open(filename, "r") as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier n'a pas été trouvé.")
class NegativeAgeError(Exception):
    pass
def set_age(age):
    if age < 0:
        raise NegativeAgeError("L'âge ne peut pas être négatif.")
    return age

class TestExceptionHandling(unittest.TestCase):

    def test_safe_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)

    def test_convert_to_int_invalid(self):
        with self.assertRaises(ValueError):
            convert_to_int("gi")

    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file("exemple.txt")

    def test_set_age_negative(self):
        with self.assertRaises(NegativeAgeError):
            set_age(-1)

if __name__ == '__main__':
    unittest.main()
