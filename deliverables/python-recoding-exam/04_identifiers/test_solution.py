import unittest
from solution import next_code
class Tests(unittest.TestCase):
    def test_next(self):
        a=["R010","R002","R099"]; self.assertEqual(next_code(a),"R100"); self.assertEqual(a,["R010","R002","R099"])
        self.assertEqual(next_code([]),"R001"); self.assertEqual(next_code(["R999"]),"R1000")
    def test_invalid(self):
        for a in (["R1"],["R000"],["R0001"],["R００１"],["R001","R001"]):
            with self.subTest(a=a), self.assertRaises(ValueError): next_code(a)
    def test_type(self):
        for a in (None, "R001", [1]):
            with self.subTest(a=a), self.assertRaises(TypeError): next_code(a)
