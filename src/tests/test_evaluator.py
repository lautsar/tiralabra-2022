import unittest
from algorithms.evaluator import Evaluator
from library.library import Library

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator(Library())

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

    def test_division_with_zero_returns_false(self):
        output = ['1', '0', '/']
        self.assertFalse(self.evaluator.evaluate(output))

    def test_simple_square_root(self):
        output = ['100', 'sqrt']
        self.assertEqual(10, self.evaluator.evaluate(output))

    def test_square_root_with_negative_value_returns_false(self):
        output = ['-4', 'sqrt']
        self.assertFalse(self.evaluator.evaluate(output))

    def test_evaluate_returns_false_if_unkown_tokens(self):
        output = ['2', '3', '?']
        self.assertFalse(self.evaluator.evaluate(output))

    def test_evaluate_returns_false_if_empty_string_is_given(self):
        output = []
        self.assertFalse(self.evaluator.evaluate(output))