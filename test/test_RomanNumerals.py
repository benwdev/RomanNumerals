import unittest
from app.RomanNumerals import RomanNumerals
 
 
class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.numerals = RomanNumerals()
 
    #check the argument is a number
    def test_convertToRoman_returns_error_message_if_arg_not_number(self):
        self.assertRaises(ValueError, self.numerals.convertToRoman, 'two')
    
    #check the argument has been provided
    def test_convetToRoman_returns_error_message_if_arg_not_provided(self):
        self.assertRaises(ValueError, self.numerals.convertToRoman, '')

    #check if the argument is greater than zero
    def test_convertToRoman_returns_error_message_if_arg_is_zero(self):
        self.assertRaises(ValueError, self.numerals.convertToRoman, 0)

    def test_convertToRoman_returns_error_message_if_arg_is_negative(self):
        self.assertRaises(ValueError, self.numerals.convertToRoman, -1)

    #check the value of 4000 or greater causes an error
    def test_convertToRoman_returns_error_message_if_arg_is_larger_than_3999(self):
        self.assertRaises(ValueError, self.numerals.convertToRoman, 4000)

    #check if decimal numbers raise an error
    def test_convertToRoman_returns_error_message_if_decimalnumbers(self):
        self.assertRaises(ValueError, self.numerals.convertToRoman, 0.5)
        
    
    #check some provided values (valid, invalid and extreme values return correct results)
    def test_convertToRoman_returns_correct_values(self):
        self.assertEqual("V", self.numerals.convertToRoman(5))
        self.assertEqual("IX", self.numerals.convertToRoman(9))
        self.assertEqual("DCCCLXIV", self.numerals.convertToRoman(864))
        self.assertEqual("MMMCMXCIX", self.numerals.convertToRoman(3999))
        

    

 
if __name__ == '__main__':
    unittest.main()
