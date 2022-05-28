import unittest
from algorithms.shunting_yard import ShuntingYard

class TestShuntingYard(unittest.TestCase):
    def setUp(self):
        self.shunting_yard = ShuntingYard()
    
    def test_simple_expression(self):
        expression = '( 2 + 3 )'
        self.assertEqual(['2', '3', '+'], self.shunting_yard.shunting_yard(expression))

    def test_simple_expression_2(self):
        expression = '( 5 - 2 ) + ( 3 - 1 )'
        self.assertEqual(['5', '2', '-', '3', '1', '-', '+'], self.shunting_yard.shunting_yard(expression))

    def test_simple_expression_3(self):
        expression = '( ( 1 + 2 ) + ( 3 + 4 ) )'
        self.assertEqual(['1', '2', '+', '3', '4', '+', '+'], self.shunting_yard.shunting_yard(expression))
    
    def test_get_correct_precedences(self):
        self.assertEqual(1, self.shunting_yard.get_precedence('+'))
        self.assertEqual(2, self.shunting_yard.get_precedence('*'))
        self.assertEqual(3, self.shunting_yard.get_precedence('^'))