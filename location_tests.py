import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        loc = Location("Colorado", 103, 120.1)
        self.assertEqual(repr(loc),"Location('Colorado', 103, 120.1)")

        loc = Location("Math Building", 13.6, -134.9)
        self.assertEqual(repr(loc),"Location('Math Building', 13.6, -134.9)")

        loc = Location("Home", -21.2, -11.4)
        self.assertEqual(repr(loc),"Location('Home', -21.2, -11.4)")

    # Add more tests!

if __name__ == "__main__":
        unittest.main()
