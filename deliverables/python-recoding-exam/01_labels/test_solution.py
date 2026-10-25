import unittest
from solution import normalize_label
class Tests(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(normalize_label("  STRAẞE \t Club\n"), "strasse club")
    def test_blank(self):
        for v in ("", " \t\n"):
            with self.subTest(v=v), self.assertRaises(ValueError): normalize_label(v)
    def test_types(self):
        for v in (None, 12, True, ["x"]):
            with self.subTest(v=v), self.assertRaises(TypeError): normalize_label(v)
