import unittest
from lib.utils import validateNumber, validate_positive_integers

class TestUtils(unittest.TestCase):
    
    def test_validateNumber_valid(self):
        self.assertTrue(validateNumber("2"))
        self.assertTrue(validateNumber("100"))
    
    def test_validateNumber_invalid_negative(self):
        self.assertFalse(validateNumber("-5"))
    
    def test_validateNumber_invalid_zero(self):
        self.assertFalse(validateNumber("0"))
    
    def test_validateNumber_invalid_one(self):
        self.assertFalse(validateNumber("1"))
    
    def test_validateNumber_invalid_non_integer(self):
        self.assertFalse(validateNumber("abc"))
        self.assertFalse(validateNumber("5.5"))
    
    def test_validate_positive_integers_valid(self):
        self.assertTrue(validate_positive_integers(10, 20))
        self.assertTrue(validate_positive_integers(1, 1))
    
    def test_validate_positive_integers_invalid_type(self):
        self.assertFalse(validate_positive_integers(10, "20"))
        self.assertFalse(validate_positive_integers("10", 20))
    
    def test_validate_positive_integers_invalid_values(self):
        self.assertFalse(validate_positive_integers(-10, 20))
        self.assertFalse(validate_positive_integers(10, -20))
        self.assertFalse(validate_positive_integers(0, 5))
        self.assertFalse(validate_positive_integers(5, 0))

if __name__ == '__main__':
    unittest.main()
