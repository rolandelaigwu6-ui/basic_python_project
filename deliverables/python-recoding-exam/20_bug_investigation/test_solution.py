import unittest, copy
from solution import transfer
class Tests(unittest.TestCase):
    def test_transfer(self):
        b={"A":10,"B":2}; self.assertIsNone(transfer(b,"A","B",3)); self.assertEqual(b,{"A":7,"B":5}); self.assertEqual(sum(b.values()),12)
    def test_rejected_unchanged(self):
        for s,t,n,e in (("A","B",11,ValueError),("A","Z",1,ValueError),("A","A",1,ValueError),("A","B",True,TypeError)):
            b={"A":10,"B":2}; old=copy.deepcopy(b)
            with self.subTest(s=s,t=t,n=n), self.assertRaises(e): transfer(b,s,t,n)
            self.assertEqual(b,old)
