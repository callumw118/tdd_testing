import unittest
from src.compare import compare, can_divide_by, password_length, password_includes_special_chars, password_acceptable, password_includes_upper_char

class TestCompare(unittest.TestCase):
    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3,1))

    def test_compare_10_15_returns_10_is_less_than_15(self):
        self.assertEqual("10 is less than 15", compare(10,15))

    def test_compare_20_20_returns_20_is_equal_to_20(self):
        self.assertEqual("20 is equal to 20", compare(20, 20))

    def test_if_nums_are_divisible_true(self):
        self.assertTrue(can_divide_by(21, 7))

    def test_if_nums_are_divisible_false(self):
        self.assertFalse(can_divide_by(5,4))

    def test_password_length(self):
        self.assertEqual(8, password_length("password"))

    def test_password_has_special_chars_true(self):
        self.assertTrue(password_includes_special_chars("password."))

    def test_password_has_special_chars_false(self):
        self.assertFalse(password_includes_special_chars("password"))

    def test_password_has_upper_case_char_true(self):
        self.assertTrue(password_includes_upper_char("paSsword"))
    
    def test_password_has_upper_case_char_false(self):
        self.assertFalse(password_includes_upper_char("password"))

    def test_is_password_acceptable_true(self):
        self.assertTrue(password_acceptable("password."))

    def test_is_password_acceptable_false(self):
        self.assertFalse(password_acceptable("pass."))
