import unittest, copy
from solution import apply_action
class Tests(unittest.TestCase):
    def make(self): return [{"id":"T1","status":"open","assigned_to":None,"notes":[{"message":"old"}]}]
    def test_route(self):
        r=self.make(); apply_action(r,"T1","assign"," A "); apply_action(r,"T1","start"); apply_action(r,"T1","resolve")
        out=apply_action(r,"T1","reopen"); self.assertEqual(out["status"],"open"); self.assertEqual(out["assigned_to"],"A")
        out["notes"][0]["message"]="new"; self.assertEqual(r[0]["notes"][0]["message"],"old")
    def test_rejection(self):
        for status,staff,action,arg in (("open",None,"start",None),("open","A","resolve",None),("resolved","A","assign","B"),("open",None,"assign"," "),("open",None,"reopen",None)):
            r=self.make(); r[0].update(status=status,assigned_to=staff); before=copy.deepcopy(r)
            with self.subTest(status=status,action=action), self.assertRaises(ValueError): apply_action(r,"T1",action,arg)
            self.assertEqual(r,before)
    def test_missing(self):
        with self.assertRaises(ValueError): apply_action(self.make(),"missing","start")
