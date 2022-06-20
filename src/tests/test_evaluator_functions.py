import unittest
from algorithms.evaluator import Evaluator
from library.library import Library

class TestEvaluatorFunctions(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator(Library())
        self.evaluator.stack.push(10)
        self.evaluator.stack.push(5)
    
    def test_take_two_returns_false_if_cannot_pop_two_values(self):
        self.evaluator.stack.pop()
        self.assertFalse(self.evaluator.take_two_values('+'))

    def test_take_one_returns_false_if_cannot_pop_value(self):
        self.evaluator.stack.pop()
        self.evaluator.stack.pop()
        self.assertFalse(self.evaluator.take_one_value('abs'))

    def test_sum(self):
        self.evaluator.take_two_values('+')
        self.assertEqual(15, self.evaluator.stack.peek())

    def test_subtraction(self):
        self.evaluator.take_two_values('-')
        self.assertEqual(5, self.evaluator.stack.peek())

    def test_multiplication(self):
        self.evaluator.take_two_values('*')
        self.assertEqual(50, self.evaluator.stack.peek())

    def test_division(self):
        self.evaluator.take_two_values('/')
        self.assertEqual(2, self.evaluator.stack.peek())

    def test_division_with_zero_returns_false(self):
        self.evaluator.stack.push(0)
        self.assertFalse(self.evaluator.take_two_values('/'))

    def test_power(self):
        self.evaluator.take_two_values('^')
        self.assertEqual(100000, self.evaluator.stack.peek())

    def test_min(self):
        self.evaluator.take_two_values('min')
        self.assertEqual(5, self.evaluator.stack.peek())

    def test_max(self):
        self.evaluator.take_two_values('max')
        self.assertEqual(10, self.evaluator.stack.peek())

    def test_unknown_token_returns_false(self):
        self.assertFalse(self.evaluator.take_one_value('?'))
        self.assertFalse(self.evaluator.take_two_values('?'))

    def test_valid_token_returns_true(self):
        self.assertTrue(self.evaluator.take_one_value('abs'))
        self.assertTrue(self.evaluator.take_two_values('+'))

    def test_sin(self):
        self.evaluator.stack.push(0)
        self.evaluator.take_one_value('sin')
        self.assertEqual(0, self.evaluator.stack.peek())

    def test_cos(self):
        self.evaluator.stack.push(0)
        self.evaluator.take_one_value('cos')
        self.assertEqual(1, self.evaluator.stack.peek())

    def test_tan(self):
        self.evaluator.stack.push(0)
        self.evaluator.take_one_value('tan')
        self.assertEqual(0, self.evaluator.stack.peek())

    def test_abs_with_positive_value(self):
        self.evaluator.take_one_value('abs')
        self.assertEqual(5, self.evaluator.stack.peek())

    def test_abs_with_negative_value(self):
        self.evaluator.stack.push(-5)
        self.evaluator.take_one_value('abs')
        self.assertEqual(5, self.evaluator.stack.peek())

    def test_sqrt(self):
        self.evaluator.stack.push(100)
        self.evaluator.take_one_value('sqrt')
        self.assertEqual(10, self.evaluator.stack.peek())

    def test_log_returns_false_with_negative_value(self):
        self.evaluator.stack.push(-5)
        self.assertFalse(self.evaluator.take_one_value('log'))

    def test_ln_returns_false_with_negative_value(self):
        self.evaluator.stack.push(-5)
        self.assertFalse(self.evaluator.take_one_value('ln'))

    def test_sqrt_returns_false_with_negative_value(self):
        self.evaluator.stack.push(-5)
        self.assertFalse(self.evaluator.take_one_value('sqrt'))

