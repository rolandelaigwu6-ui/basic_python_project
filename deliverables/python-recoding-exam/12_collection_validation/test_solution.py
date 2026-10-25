import unittest, copy
from solution import validate_batches
class Tests(unittest.TestCase):
    def test_scoped_uniqueness(self):
        r=[dict(id=i,notes=[dict(note_id="N1",message="ok")]) for i in ("A","B")]; old=copy.deepcopy(r)
        self.assertIsNone(validate_batches(r)); self.assertEqual(r,old)
    def test_invalid(self):
        cases=[([dict(id="A",notes=[]),dict(id="A",notes=[])],ValueError),([dict(id="A",notes=[dict(note_id="N1",message="x"),dict(note_id="N1",message="y")])],ValueError),([dict(id="A",notes=[]),dict(id="B")],ValueError),([dict(id="A",notes=None)],TypeError),(None,TypeError)]
        for r,e in cases:
            old=copy.deepcopy(r)
            with self.subTest(r=r), self.assertRaises(e): validate_batches(r)
            self.assertEqual(r,old)
