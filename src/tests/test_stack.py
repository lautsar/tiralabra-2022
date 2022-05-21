import unittest
from structures.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    
    def test_initialize_correctly(self):
        self.assertEqual([], self.stack.stack)
        self.assertEqual(-1, self.stack.top)

    def test_push_works_correctly(self):
        self.stack.push(4)
        self.assertEqual([4], self.stack.stack)
        self.assertEqual(0, self.stack.top)

    def test_push_multiple_times_works_correctly(self):
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual([4, 3], self.stack.stack)
        self.assertEqual(1, self.stack.top)

    def test_pop_returns_false_if_stack_is_empty(self):
        self.assertFalse(self.stack.pop())

    def test_pop_returns_top(self):
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual(3, self.stack.pop())

    def test_pointer_to_top_works_with_operators(self):
        self.assertEqual(-1, self.stack.top)
        self.stack.push(4)
        self.assertEqual(0, self.stack.top)
        self.stack.push(4)
        self.assertEqual(1, self.stack.top)
        self.stack.pop()
        self.assertEqual(0, self.stack.top)

    def test_peek_returns_false_when_stack_is_empty(self):
        self.assertFalse(self.stack.peek())

    def test_peek_returns_value_on_top(self):
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual(3, self.stack.peek())
    
    def test_get_stack_returns_stack(self):
        self.assertEqual([], self.stack.get_stack())
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual([4,3], self.stack.get_stack())