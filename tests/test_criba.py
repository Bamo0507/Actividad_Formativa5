import unittest
from criba import criba

class TestCriba(unittest.TestCase):
    
    def test_criba_basic(self):
        self.assertEqual(criba(10), [2, 3, 5, 7])
        self.assertEqual(criba(2), [2])
        self.assertEqual(criba(1), [])
    
    def test_criba_large_number(self):
        primes_up_to_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(criba(30), primes_up_to_30)
    
    def test_criba_no_primes(self):
        self.assertEqual(criba(0), [])
        self.assertEqual(criba(1), [])
    
    def test_criba_non_integer(self):
        with self.assertRaises(TypeError):
            criba(10.5)
        with self.assertRaises(TypeError):
            criba("10")
    
    def test_criba_negative_number(self):
        self.assertEqual(criba(-10), [])

if __name__ == '__main__':
    unittest.main()
