import unittest
from unittest.mock import Mock
from solution import read_answer
class Tests(unittest.TestCase):
    def test_retry(self):
        inp=Mock(side_effect=["X",""," b ","A"]); out=Mock()
        self.assertEqual(read_answer("Choice: ",inp,out),"B"); self.assertEqual(inp.call_count,3); self.assertEqual(out.call_count,2)
        out.assert_called_with("Invalid choice. Enter A, B, C or D.")
    def test_terminal_end(self):
        for e in (EOFError,KeyboardInterrupt):
            with self.subTest(e=e), self.assertRaises(e): read_answer("?",Mock(side_effect=e),Mock())
