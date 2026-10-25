import unittest, tempfile, json, copy, os
from pathlib import Path
from unittest.mock import patch
from solution import save_snapshot
class Tests(unittest.TestCase):
    def test_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"data.json"; r=[{"name":"Café","notes":[{"id":"N001"}]}]; old=copy.deepcopy(r)
            self.assertIsNone(save_snapshot(r,p)); self.assertEqual(json.loads(p.read_text(encoding="utf-8")),r); self.assertEqual(r,old)
    def test_encode_failure(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"data.json"; p.write_text("original")
            for r,e in (([{} ,{"x":object()}],TypeError),([{"x":float("nan")}],ValueError),([1],TypeError)):
                with self.subTest(r=r), self.assertRaises(e): save_snapshot(r,p)
                self.assertEqual(p.read_text(),"original"); self.assertEqual(set(Path(d).iterdir()),{p})
    def test_replace_failure(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"data.json"; p.write_text("original")
            with patch("os.replace",side_effect=OSError("simulated")):
                with self.assertRaises(OSError): save_snapshot([{"x":1}],p)
            self.assertEqual(p.read_text(),"original"); self.assertEqual(set(Path(d).iterdir()),{p})
