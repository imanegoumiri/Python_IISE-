import unittest
from src.math_operations import add, subtract, multiply, divide
from src.string_operations import concatenate, uppercase

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_concatenate(self):
        self.assertEqual(concatenate("Hello ", "World!"), "Hello World!")
    def test_uppercase(self):
        self.assertEqual(uppercase("iise"), "IISE")

if __name__ == "__main__":
    unittest.main()