import unittest
from challenges.fibonacci import generate_fibonacci

class FibonacciTest(unittest.TestCase):

    def test_generate_fibo(self):
        self.assertTrue(generate_fibonacci(1), [0])
        self.assertTrue(generate_fibonacci(2), [0,1])
        self.assertTrue(generate_fibonacci(3), [0,1,1])
        self.assertTrue(generate_fibonacci(4), [0,1,1,2])
        self.assertTrue(generate_fibonacci(5), [0,1,1,2,3])
        self.assertTrue(generate_fibonacci(9), [0,1,1,2,3,5,8,13,21])
