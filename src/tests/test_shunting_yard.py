import unittest
from algorithms.shunting_yard import ShuntingYard
from library.library import Library

class TestShuntingYard(unittest.TestCase):
    def setUp(self):
        self.shunting_yard = ShuntingYard(Library())
    
    def test_simple_expression(self):
        expression = '(2+3)'
        self.assertEqual(['2', '3', '+'], self.shunting_yard.shunting_yard(expression))

    def test_simple_expression_2(self):
        expression = '(5-2) + ( 3 - 1 )'
        self.assertEqual(['5', '2', '-', '3', '1', '-', '+'], self.shunting_yard.shunting_yard(expression))

    def test_simple_expression_3(self):
        expression = '( ( 1 + 2 ) + ( 3 + 4 ) )'
        self.assertEqual(['1', '2', '+', '3', '4', '+', '+'], self.shunting_yard.shunting_yard(expression))
    
    def test_simple_expression_with_negative_value(self):
        expression = '(-2) + 3'
        self.assertEqual(['-2', '3', '+'], self.shunting_yard.shunting_yard(expression))

    def test_more_complicated_expression(self):
        expression = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
        self.assertEqual(['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+'], self.shunting_yard.shunting_yard(expression))
    
    def test_get_correct_precedences(self):
        self.assertEqual(2, self.shunting_yard.get_precedence('+')[0])
        self.assertEqual(3, self.shunting_yard.get_precedence('*')[0])
        self.assertEqual(4, self.shunting_yard.get_precedence('^')[0])