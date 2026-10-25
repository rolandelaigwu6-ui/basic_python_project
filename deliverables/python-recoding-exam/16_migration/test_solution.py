import unittest, copy
from solution import upgrade_records
class Tests(unittest.TestCase):
    def test_migration(self):
        r=[{"id":"A","extra":{"x":1}},{"id":"B","notes":["old"]}]; before=copy.deepcopy(r); out=upgrade_records(r)
        self.assertEqual(out[0]["notes"],[]); self.assertEqual(out[1]["notes"],["old"]); out[0]["extra"]["x"]=9; self.assertEqual(r,before)
    def test_late_failure(self):
        for last,e in (({"id":"B","notes":None},TypeError),({"id":"A"},ValueError),({"notes":[]},ValueError)):
            r=[{"id":"A"},last]; before=copy.deepcopy(r)
            with self.subTest(last=last), self.assertRaises(e): upgrade_records(r)
            self.assertEqual(r,before)
