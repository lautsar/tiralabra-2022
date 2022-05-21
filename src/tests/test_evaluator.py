import unittest
from algorithms.evaluator import Evaluator

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator()

    def test_simple_sum(self):
        output = ['2', '3', '+']
        self.assertEqual(5, self.evaluator.evaluate(output))

    def test_simple_subtraction(self):
        output = ['2', '3', '-']
        self.assertEqual(-1, self.evaluator.evaluate(output))

    def test_simple_multiplication(self):
        output = ['2', '3', '*']
        self.assertEqual(6, self.evaluator.evaluate(output))

    def test_simple_division(self):
        output = ['10', '5', '/']
        self.assertEqual(2.0, self.evaluator.evaluate(output))

    def test_simple_power(self):
        output = ['2', '3', '^']
        self.assertEqual(8, self.evaluator.evaluate(output))

    def test_evaluate_returns_false_if_unkown_tokens(self):
        output = ['2', '3', '?']
        self.assertFalse(self.evaluator.evaluate(output))