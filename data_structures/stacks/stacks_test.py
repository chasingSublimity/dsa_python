import unittest

from stacks import Stack
from node import Node

class StackTest(unittest.TestCase):
    def test_create_new_stack(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        self.assertEqual(stack.limit, 1000)
        self.assertIsNone(stack.head)

    def test_has_space(self):
        stack = Stack(1)
        self.assertEqual(stack.has_space(), True)
        stack.push(5)
        self.assertEqual(stack.has_space(), False)

    def test_is_empty(self):
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)
        stack.push(5)
        self.assertEqual(stack.is_empty(), False)

    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertIsInstance(stack.head, Node)
        self.assertEqual(stack.head.value, 5)
        self.assertEqual(len(stack), 1)

    def test_prevent_stack_overflow(self):
        stack = Stack(1)
        stack.push(5)
        with self.assertRaises(IndexError):
            stack.push(6)

    def test_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(len(stack), 0)

    def test_peak(self):
        stack = Stack()
        self.assertIsNone(stack.peak())
        stack.push(5)
        self.assertEqual(stack.peak(), 5)
        self.assertEqual(len(stack), 1)


if __name__ == '__main__':
    unittest.main()