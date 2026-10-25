import unittest
from solution import decode_catalog
class Tests(unittest.TestCase):
    def test_valid(self): self.assertEqual(decode_catalog('[{"id":"A","name":"Café","quantity":0}]')[0]["name"],"Café")
    def test_invalid(self):
        for s in ('{','null','{}','[1]','[{"id":"A","name":"X","quantity":true}]','[{"id":"A","name":"X","quantity":1},{"id":"A","name":"Y","quantity":2}]','[{"id":"A","name":"X","quantity":1,"quantity":2}]','[{"id":"A","quantity":1}]'):
            with self.subTest(s=s), self.assertRaises(ValueError): decode_catalog(s)
    def test_type(self):
        with self.assertRaises(TypeError): decode_catalog(None)
