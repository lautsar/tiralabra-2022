import unittest
import math
from library.constants import Constants

class TestConstansts(unittest.TestCase):
    def setUp(self):
        self.constants = Constants()
    
    def test_initialize_correctly(self):
        self.assertEqual(2, len(self.constants.constants))

    def test_get_value_returns_correct_value(self):
        self.assertEqual(math.pi, self.constants.get_value('pi'))
        self.assertEqual(math.e, self.constants.get_value('e'))

    def test_get_value_returns_false_if_not_found(self):
        self.assertFalse(self.constants.get_value('error'))

    def test_list_usable_constants_returns_correct_list(self):
        self.assertEqual(['pi', 'e'], self.constants.list_usable_constants())