import unittest
from library.functions import Functions

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.functions = Functions()
    
    def test_initialize_correctly(self):
        self.assertEqual(6, len(self.functions.functions))

    def test_get_value_returns_correct_number_of_parameters(self):
        self.assertEqual(2, self.functions.get_value('min'))
        self.assertEqual(1, self.functions.get_value('sin'))

    def test_get_value_returns_false_if_not_found(self):
        self.assertFalse(self.functions.get_value('error'))

    def test_list_usable_constants_returns_correct_list(self):
        self.assertEqual(['min', 'max', 'sqrt', 'sin', 'cos', 'tan'], 
                        self.functions.list_usable_functions())