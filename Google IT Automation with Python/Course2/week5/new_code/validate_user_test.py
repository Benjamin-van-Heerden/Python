import unittest
from validate_user import is_valid_username

class TestValidUser(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(is_valid_username("Benjamin", 3), True)

    def test_two(self):
        self.assertEqual(is_valid_username("b-en-min", 4), False)

    def test_three(self):
        self.assertEqual(is_valid_username("benja123", 25), False)

    def test_three(self):
        self.assertEqual(is_valid_username("benja123", 3), True)

    def test_four(self):
        self.assertRaises(ValueError, is_valid_username, "Name", -1)

    
if __name__ == "__main__":
    unittest.main()