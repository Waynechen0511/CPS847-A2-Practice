import unittest
from Functions import add2, add3

class TestFunctions(unittest.TestCase):
    """
    Test Harness
    """

    def test_add2(self):
        """test add 2"""
        self.assertEqual(add2(2), 4)
        self.assertEqual(add2(3), 5)
        self.assertEqual(add2(4), 6)

    def test_add3(self):
        """test add 3"""
        self.assertEqual(add3(2), 5)
        self.assertEqual(add3(3), 6)
        self.assertEqual(add3(4), 7)

if __name__ == "__main__":
    unittest.main()