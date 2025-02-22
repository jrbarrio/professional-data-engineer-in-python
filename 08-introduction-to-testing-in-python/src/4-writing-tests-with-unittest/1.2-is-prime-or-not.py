import unittest
import math

def is_prime(num):
    if num == 1: return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 17 is prime
        self.assertTrue(is_prime(17))

    def test_is_not_prime(self):
        # Check that 6 is not prime
        self.assertFalse(is_prime(6))