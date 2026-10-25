import unittest, copy
from solution import reserve_stock
class Tests(unittest.TestCase):
    def test_success(self):
        x={"A":{"stock":5,"meta":[1]},"B":{"stock":2}}
        self.assertEqual(reserve_stock(x,"A",3),2); self.assertEqual(x["B"]["stock"],2); self.assertEqual(x["A"]["meta"],[1])
    def test_unchanged(self):
        for code,n,e in (("A",6,ValueError),("Z",1,ValueError),("A",0,ValueError),("A",True,TypeError),("A",1.5,TypeError),(1,1,TypeError)):
            x={"A":{"stock":5,"notes":[{"x":1}]}}; before=copy.deepcopy(x)
            with self.subTest(code=code,n=n), self.assertRaises(e): reserve_stock(x,code,n)
            self.assertEqual(x,before)
