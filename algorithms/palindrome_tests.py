import unittest
from algorithms.palindrome import Solution


class PalindromeTest(unittest.TestCase):
    def test_empty(self):
        result = Solution().is_palindrom("")
        self.assertTrue(result, msg="'' should be a palindrome")

    def test_simple_false(self):
        result = Solution().is_palindrom("Hello World")
        self.assertFalse(result, msg="'' should not be a palindrome")

    def test_simple_true(self):
        result = Solution().is_palindrom("A Toyota’s a Toyota")
        self.assertTrue(result, msg="'' should be a palindrome")

    def test_simple_false_num(self):
        result = Solution().is_palindrom("A Toyota’s a Toyota1")
        self.assertFalse(result, msg="'' should not be a palindrome")

    def test_simple_true_num(self):
        result = Solution().is_palindrom("A22 Toyota’s a Toyot22a")
        self.assertTrue(result, msg="'' should be a palindrome")

    def test_special_char_true(self):
        result = Solution().is_palindrom("87A_ T$oyota’s{} a T|oyot**a?78")
        self.assertTrue(result, msg="'' should be a palindrome")


if __name__ == '__main__':
    unittest.main()
