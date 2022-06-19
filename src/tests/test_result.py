import unittest
from algorithms.shunting_yard import ShuntingYard
from algorithms.evaluator import Evaluator
from library.library import Library

class TestResult(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.shunting_yard = ShuntingYard(self.library)
        self.evaluator = Evaluator(self.library)

    def test_simple_sum(self):
        expression = '2+3'
        output = self.shunting_yard.shunting_yard(expression)
        result = self.evaluator.evaluate(output)

        self.assertEqual(5, result)

    def test_simple_expression(self):
        expression = '2^0+3^3'
        output = self.shunting_yard.shunting_yard(expression)
        result = self.evaluator.evaluate(output)

        self.assertEqual(28, result)

    def test_simple_function(self):
        expression = 'sqrt(100)'
        output = self.shunting_yard.shunting_yard(expression)
        result = self.evaluator.evaluate(output)

        self.assertEqual(10, result)

    def test_expression_with_multiple_operations(self):
        expression = 'sqrt(100)-3^2-min(9,1)'
        output = self.shunting_yard.shunting_yard(expression)
        result = self.evaluator.evaluate(output)

        self.assertEqual(0, result)

    def test_trigonometric_functions(self):
        expression = 'sin(pi/2)+cos(pi)'
        output = self.shunting_yard.shunting_yard(expression)
        result = self.evaluator.evaluate(output)

        self.assertEqual(0, result)

    def test_simple_expression_with_negative_values(self):
        expression = '2*4+(-3)'
        output = self.shunting_yard.shunting_yard(expression)
        result = self.evaluator.evaluate(output)

        self.assertEqual(5, result)

    def test_simple_expression_with_negative_values2(self):
        expression = '2.5+4.25+(-3.5)'
        output = self.shunting_yard.shunting_yard(expression)
        result = self.evaluator.evaluate(output)

        self.assertEqual(3.25, result)
