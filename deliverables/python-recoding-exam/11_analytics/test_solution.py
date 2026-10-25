import unittest, copy
from solution import summarize
class Tests(unittest.TestCase):
    def test_empty(self):
        r=summarize([]); self.assertEqual(r["resolution_percentage"],0.0); self.assertEqual(r["total"],0)
        self.assertEqual(r["by_status"],dict(open=0,in_progress=0,resolved=0)); self.assertEqual(set(r["by_category"]),{"Network","Hardware","Software","Other"})
    def test_counts_reopen(self):
        data=[dict(status=s,priority=p,category=c) for s,p,c in [("open","high","Network"),("in_progress","low","Other"),("resolved","high","Network")]]; before=copy.deepcopy(data)
        r=summarize(data); self.assertEqual(r["unresolved"],2); self.assertAlmostEqual(r["resolution_percentage"],100/3); self.assertEqual(r["by_category"]["Network"],2)
        for k in ("by_status","by_priority","by_category"): self.assertEqual(sum(r[k].values()),3)
        self.assertEqual(data,before); data[2]["status"]="open"; self.assertEqual(summarize(data)["resolved"],0)
