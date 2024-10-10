import unittest
from euclidean import euclidean

class TestEuclidean(unittest.TestCase):
    
    def test_euclidean_basic(self):
        self.assertEqual(euclidean(60, 48), 12)
        self.assertEqual(euclidean(100, 10), 10)
    
    def test_euclidean_primes(self):
        self.assertEqual(euclidean(13, 7), 1)
        self.assertEqual(euclidean(17, 31), 1)
    
    def test_euclidean_same_number(self):
        self.assertEqual(euclidean(25, 25), 25)
    
    def test_euclidean_one_number_zero(self):
        with self.assertRaises(ValueError):
            euclidean(10, 0)
        with self.assertRaises(ValueError):
            euclidean(0, 10)
    
    def test_euclidean_negative_numbers(self):
        with self.assertRaises(ValueError):
            euclidean(-10, 5)
        with self.assertRaises(ValueError):
            euclidean(10, -5)
        with self.assertRaises(ValueError):
            euclidean(-10, -5)
    
    def test_euclidean_non_integer(self):
        with self.assertRaises(ValueError):
            euclidean(10.5, 5)
        with self.assertRaises(ValueError):
            euclidean(10, "5")
        with self.assertRaises(ValueError):
            euclidean("10", "5")

if __name__ == '__main__':
    unittest.main()
