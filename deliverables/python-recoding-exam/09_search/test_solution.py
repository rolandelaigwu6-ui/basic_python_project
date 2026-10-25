import unittest, copy
from solution import find_records
class Tests(unittest.TestCase):
    def fixture(self):
        return [dict(id="A",title="WI-FI down",category="Network",status="open",priority="high",notes=[{"x":1}]),dict(id="B",title="wi-fi setup",category="Software",status="open",priority="low",notes=[]),dict(id="C",title="wi-fi slow",category="Network",status="resolved",priority="high",notes=[])]
    def test_and(self):
        r=self.fixture(); before=copy.deepcopy(r)
        out=find_records(r," WI-FI "," network ","OPEN","high"); self.assertEqual([x["id"] for x in out],["A"])
        out[0]["notes"][0]["x"]=9; self.assertEqual(r,before)
    def test_empty_and_punctuation(self):
        self.assertEqual(len(find_records(self.fixture())),3); self.assertEqual(find_records(self.fixture(),"wifi"),[])
    def test_invalid_empty(self):
        with self.assertRaises(ValueError): find_records([],status="closed")
        with self.assertRaises(TypeError): find_records([],text=None)
