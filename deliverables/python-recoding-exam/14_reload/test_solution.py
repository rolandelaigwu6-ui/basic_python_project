import unittest, tempfile, copy
from pathlib import Path
from solution import reload_catalog
class Tests(unittest.TestCase):
    def test_success(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.json"; p.write_text('[{"id":"A","name":"Café","quantity":2}]',encoding="utf-8")
            c=[{"old":[1]}]; ident=id(c); self.assertIsNone(reload_catalog(c,p)); self.assertEqual(id(c),ident); self.assertEqual(c[0]["name"],"Café")
            p.write_text('[]'); reload_catalog(c,p); self.assertEqual(c,[])
    def test_failure_unchanged(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.json"
            for content in ('{','[{"id":"A","name":"X","quantity":1},{"id":"A","name":"Y","quantity":2}]'):
                p.write_text(content); c=[{"old":[1]}]; before=copy.deepcopy(c)
                with self.assertRaises(ValueError): reload_catalog(c,p)
                self.assertEqual(c,before); self.assertEqual(p.read_text(),content)
            with self.assertRaises(OSError): reload_catalog(c,Path(d)/"missing")
            self.assertEqual(c,before)
