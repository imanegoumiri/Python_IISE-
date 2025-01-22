import unittest
from Ex1 import conversion

class TestConversion(unittest.TestCase):
    def test_dollars_to_dirhams(self):
        self.assertEqual(conversion.dollars_to_dirhams(200), 2000)

    def test_meters_to_kilometers(self):
        self.assertEqual(conversion.meters_to_kilometers(5000), 5)

if __name__ == "__main__":
    unittest.main()
