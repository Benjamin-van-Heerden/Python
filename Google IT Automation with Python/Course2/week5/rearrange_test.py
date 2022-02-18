import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(rearrange_name("Lovelace, Ada"), "Ada Lovelace")

    def test_edge1(self):
        self.assertEqual(rearrange_name("Person H., S. Man"), "S. Man Person H.")

    def test_empty(self):
        self.assertEqual(rearrange_name(""), None)

    def test_strange_name(self):
        self.assertEqual(rearrange_name("K-52 is a driving manual"), None)

    def test_one_name(self):
        self.assertEqual(rearrange_name("Voltaire"), "Voltaire")

if __name__ == "__main__":
    unittest.main()

