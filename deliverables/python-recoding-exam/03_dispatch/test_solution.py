import unittest
from solution import dispatch_level
class Tests(unittest.TestCase):
    def test_matrix(self):
        expected={"low":["low","low","medium","medium","high","high"],"medium":["medium"]*4+["high","high"],"high":["high"]*4+["critical","critical"]}
        for s, levels in expected.items():
            for n, level in zip((1,2,3,9,10,11),levels):
                with self.subTest(s=s,n=n): self.assertEqual(dispatch_level(s,n),level)
    def test_invalid(self):
        for s,n,e in (("HIGH",1,ValueError),("low",0,ValueError),("low",True,TypeError),(None,2,TypeError)):
            with self.subTest(s=s,n=n), self.assertRaises(e): dispatch_level(s,n)
