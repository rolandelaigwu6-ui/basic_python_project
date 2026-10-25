import unittest, copy
from unittest.mock import Mock
from solution import run_check
class Tests(unittest.TestCase):
    def test_session(self):
        b=[dict(id=f"Q{i+1}",prompt=f"Scenario {i+1}",options={c:f"option {c}" for c in "ABCD"},correct=c) for i,c in enumerate("BCBCCB")]; old=copy.deepcopy(b)
        inp=Mock(side_effect=["X"," b ","A","B","C","C","B"," "," First reason ","Second reason"]); lines=[]
        out=run_check(b,inp,lambda *a: lines.append(" ".join(map(str,a))))
        self.assertEqual(out,{"answers":list("B ABCCB".replace(" ","")),"score":5,"explanations":{"Q1":"First reason","Q2":"Second reason"}})
        self.assertEqual(inp.call_count,10); self.assertEqual(b,old); self.assertIn("Score: 5/6","\n".join(lines))
        text="\n".join(lines)
        for q in b: self.assertIn(q["prompt"],text)
        for c in "ABCD": self.assertIn(f"option {c}",text)
    def test_eof(self):
        b=[dict(id=str(i),prompt="?",options={c:c for c in "ABCD"},correct="A") for i in range(6)]
        with self.assertRaises(EOFError): run_check(b,Mock(side_effect=EOFError),Mock())
