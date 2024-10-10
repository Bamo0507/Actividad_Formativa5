import unittest
from bezout import bezout

class TestBezout(unittest.TestCase):
    
    def test_bezout_basic(self):
        self.assertEqual(bezout(120, 68), (4, -7))
        self.assertEqual(bezout(60, 48), (1, -1))
        self.assertEqual(bezout(35, 15), (1, -2))
    
    def test_bezout_primes(self):
        # For coprime numbers, ax + by = 1
        x, y = bezout(17, 31)
        self.assertEqual(17 * x + 31 * y, 1)
    
    # def test_bezout_same_number(self):
    #     self.assertEqual(bezout(25, 25), (1, 0))
    
    def test_bezout_one_number_zero(self):
        with self.assertRaises(ValueError):
            bezout(10, 0)
        with self.assertRaises(ValueError):
            bezout(0, 10)
    
    def test_bezout_negative_numbers(self):
        with self.assertRaises(ValueError):
            bezout(-10, 5)
        with self.assertRaises(ValueError):
            bezout(10, -5)
        with self.assertRaises(ValueError):
            bezout(-10, -5)
    
    def test_bezout_non_integer(self):
        with self.assertRaises(ValueError):
            bezout(10.5, 5)
        with self.assertRaises(ValueError):
            bezout(10, "5")
        with self.assertRaises(ValueError):
            bezout("10", "5")

if __name__ == '__main__':
    unittest.main()
