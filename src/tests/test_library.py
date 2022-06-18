import unittest
import math
from library.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.variables.add_variable('a', 100)
        self.library.variables.add_variable('b', 200)

    def test_get_variables_returns_variables(self):
        self.assertEqual(2, len(self.library.get_variables()))
        self.assertEqual(['a', 'b'], self.library.get_variables())

    def test_get_variable_values_returns_corrects_value(self):
        self.assertFalse(self.library.get_variable_value('x'))
        self.assertEqual(100, self.library.get_variable_value('a'))

    def test_get_constants_returns_constants(self):
        self.assertEqual(2, len(self.library.get_constants()))
        self.assertEqual(['pi', 'e'], self.library.get_constants())

    def test_get_constant_values_returns_corrects_value(self):
        self.assertFalse(self.library.get_constant_value('x'))
        self.assertEqual(math.pi, self.library.get_constant_value('pi'))

    def test_get_functions_returns_functions(self):
        self.assertEqual(6, len(self.library.get_functions()))

    def test_get_operators_returns_operators(self):
        self.assertEqual(5, len(self.library.get_operators()))

    def test_add_variables_returns_correct_values(self):
        self.assertTrue(self.library.add_variable('c', 100))