import unittest
import math
from library.variables import Variables

class TestVariables(unittest.TestCase):
    def setUp(self):
        self.variables = Variables()
    
    def test_initialize_correctly(self):
        self.assertEqual(0, len(self.variables.variables))

    def test_get_value_returns_correct_value(self):
        self.variables.add_variable('a', 100)

        self.assertEqual(100, self.variables.get_value('a'))

    def test_get_value_returns_false_if_not_found(self):
        self.assertFalse(self.variables.get_value('x'))

    def test_list_used_variables_returns_correct_list(self):
        self.assertEqual([], self.variables.list_used_variables())

        self.variables.add_variable('a', 100)
        self.variables.add_variable('b', 200)

        self.assertEqual(['a', 'b'], self.variables.list_used_variables())

    def test_update_variable_returns_false_if_not_found(self):
        self.assertFalse(self.variables.update_value('x', 100))

    def test_update_variable_changes_value(self):
        self.variables.add_variable('x', 100)
        self.assertEqual(100, self.variables.get_value('x'))

        self.variables.update_value('x', 200)
        self.assertEqual(200, self.variables.get_value('x'))

    def test_adding_existing_updates_value(self):
        self.variables.add_variable('a', 100)
        self.variables.add_variable('b', 100)
        self.variables.add_variable('c', 100)

        self.assertEqual(3, len(self.variables.variables))
        self.assertEqual(100, self.variables.get_value('b'))

        self.variables.add_variable('b', 200)

        self.assertEqual(3, len(self.variables.variables))
        self.assertEqual(200, self.variables.get_value('b'))