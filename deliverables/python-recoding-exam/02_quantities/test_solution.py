import unittest
from solution import validate_quantity
class Tests(unittest.TestCase):
    def test_boundaries(self):
        for n in (1, 250, 500): self.assertEqual(validate_quantity(n), n)
    def test_range(self):
        for n in (0, -1, 501):
            with self.subTest(n=n), self.assertRaises(ValueError): validate_quantity(n)
    def test_types(self):
        class MyInt(int): pass
        for v in (True, False, 1.0, "3", None, MyInt(2)):
            with self.subTest(v=v), self.assertRaises(TypeError): validate_quantity(v)
