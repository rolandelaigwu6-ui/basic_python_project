import unittest, copy
from solution import validate_device
class Tests(unittest.TestCase):
    def test_valid(self):
        r=dict(serial="D1",label="Laptop",stock=2,state="available",extra=[1]); old=copy.deepcopy(r)
        self.assertIsNone(validate_device(r)); self.assertEqual(r,old)
    def test_invariants(self):
        base=dict(serial="D1",label="Laptop",stock=2,state="available")
        for change in ({"stock":-1},{"state":"retired"},{"label":" x "},{"serial":""}):
            r=base|change; old=copy.deepcopy(r)
            with self.subTest(change=change), self.assertRaises(ValueError): validate_device(r)
            self.assertEqual(r,old)
        del base["serial"]
        with self.assertRaises(ValueError): validate_device(base)
    def test_types(self):
        with self.assertRaises(TypeError): validate_device([])
        with self.assertRaises(TypeError): validate_device(dict(serial="D1",label="X",stock=True,state="available"))
