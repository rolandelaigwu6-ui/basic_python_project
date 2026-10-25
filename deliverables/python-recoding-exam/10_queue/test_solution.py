import unittest, copy
from solution import open_queue
class Tests(unittest.TestCase):
    def test_order_and_filter(self):
        r=[dict(id=i,status=s,priority=p,notes=[{"x":1}]) for i,s,p in [("T010","open","high"),("T002","open","high"),("T001","in_progress","critical"),("T003","open","critical"),("T004","resolved","critical"),("T005","open","low"),("T006","open","medium")]]
        old=copy.deepcopy(r); out=open_queue(r); self.assertEqual([x["id"] for x in out],["T003","T002","T010","T006","T005"])
        out[0]["notes"][0]["x"]=5; self.assertEqual(r,old)
    def test_empty(self): self.assertEqual(open_queue([]),[])
