import unittest
from my_prime_numbers.prime_numbers import is_prime, generate_primes

class TestPrimeNumbers(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

    def test_generate_primes(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])
        self.assertEqual(generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(generate_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

if name == '__main__':
    unittest.main()
