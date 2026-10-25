import unittest, copy
from solution import append_note
class Tests(unittest.TestCase):
    def test_ids_and_isolation(self):
        r={"status":"open","notes":[{"note_id":"N010","author":"A","message":"older"},{"note_id":"N002","author":"B","message":"older"}]}
        n=append_note(r," C "," hello "); self.assertEqual(n,{"note_id":"N011","author":"C","message":"hello"})
        n["message"]="changed"; self.assertEqual(r["notes"][-1]["message"],"hello")
    def test_boundaries(self):
        for n in (5,300): self.assertEqual(len(append_note({"status":"in_progress","notes":[]},"A","x"*n)["message"]),n)
    def test_rejection(self):
        for status,a,m,e in (("resolved","A","hello",ValueError),("open"," ","hello",ValueError),("open","A","abcd",ValueError),("open","A","x"*301,ValueError),("open","A",None,TypeError)):
            r={"status":status,"notes":[]}; before=copy.deepcopy(r)
            with self.subTest(status=status,a=a), self.assertRaises(e): append_note(r,a,m)
            self.assertEqual(r,before)
        r={"status":"open","notes":[]}
        with self.assertRaises(ValueError): append_note(r,"A","bad")
        self.assertEqual(append_note(r,"A","valid")["note_id"],"N001")
