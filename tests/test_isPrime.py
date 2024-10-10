import unittest
from isPrime import Test_Primalidad

class TestIsPrime(unittest.TestCase):
    
    def test_is_prime_true(self):
        self.assertTrue(Test_Primalidad(2))
        self.assertTrue(Test_Primalidad(3))
        self.assertTrue(Test_Primalidad(5))
        self.assertTrue(Test_Primalidad(29))
        self.assertTrue(Test_Primalidad(97))
    
    def test_is_prime_false(self):
        self.assertEqual(Test_Primalidad(4), 2)
        self.assertEqual(Test_Primalidad(6), 2)
        self.assertEqual(Test_Primalidad(9), 3)
        self.assertEqual(Test_Primalidad(15), 3)
        self.assertEqual(Test_Primalidad(100), 2)
    
    def test_is_prime_large_prime(self):
        self.assertTrue(Test_Primalidad(104729))  # Número primo significativamente grande
    
    def test_is_prime_large_composite(self):
        self.assertEqual(Test_Primalidad(104730), 2)
    
    # def test_is_prime_non_integer(self):
    #     with self.assertRaises(TypeError):
    #         Test_Primalidad(10.5)
    #     with self.assertRaises(TypeError):
    #         Test_Primalidad("10")
    
    # def test_is_prime_negative_number(self):
    #     self.assertEqual(Test_Primalidad(-5), 5)
    
    def test_is_prime_one(self):
        self.assertEqual(Test_Primalidad(1), True)

if __name__ == '__main__':
    unittest.main()
