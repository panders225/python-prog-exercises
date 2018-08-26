

import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_seven_prime(self):
        """Is seven successfully determined to be prime?"""
        self.assertTrue(is_prime(7))

    def test_is_four_prime(self):
        """Is four successfully determined to be prime?"""
        self.assertTrue(is_prime(4), msg="Four is not prime!")

    def test_is_zero_prime(self):
        """Is zero corretly determined to not be prime"""
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        """Is a negative number correctly determined to not be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))

if __name__ == '__main__':
    unittest.main()
