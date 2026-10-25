import unittest, copy
from solution import score_answers
class Tests(unittest.TestCase):
    def test_score(self):
        b=[{"id":"Q2","correct":"C"},{"id":"Q1","correct":"B"},{"id":"Q9","correct":"D"}]; old=copy.deepcopy(b)
        self.assertEqual(score_answers(b,["C","A","D"]),2); self.assertEqual(b,old); self.assertEqual(score_answers([],[]),0)
    def test_invalid(self):
        for b,a in (([{"id":"Q","correct":"A"}],[]),([{ "id":"Q","correct":"A"}],["a"]),([{ "id":"Q","correct":"A"},{"id":"Q","correct":"B"}],["A","B"]),([{"id":"Q"}],["A"])):
            with self.subTest(b=b,a=a), self.assertRaises(ValueError): score_answers(b,a)
