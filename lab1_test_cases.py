import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_ValueError(self):
        """Testing iterative function to find and out put maximum value index"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_max_at_end(self):
        self.assertEqual(max_list_iter([1,4,8,11]), 11)

    def test_max_list_iter_max_at_beginning(self):
        self.assertEqual(max_list_iter([11,1,9,6]), 11)

    def test_max_list_iter_all_negative_nums(self):
        self.assertEqual(max_list_iter([-30,-11,-26,-3]),-3)

    def test_max_list_iter_positive_and_negative_list(self):
        self.assertEqual(max_list_iter([-5,4,2,0,-26]), 4)

    """Testing recursive function to reverse the input list"""
    def test_reverse_rec_ValueError(self):

       tlist = None
       with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_regularlist(self):
       self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_singleval_list(self):
       self.assertEqual(reverse_rec([1]),[1])

    def test_reverse_rec_list_with_negatives(self):
       self.assertEqual(reverse_rec([-1,0,1]),[1,0,-1])

    def test_reverse_rec_list_empty(self):
       self.assertEqual(reverse_rec([]),[])

    """Testing recursive binary search funciton"""
    def test_bin_search_ValueError(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_bin_search_firstval(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )

    def test_bin_search_lastval(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )

    def test_bin_search_midvalcenter(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_midvallower(self):
        list_val =[0,1,2,11,4,7,8,9]
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), 3 )

    def test_bin_search_midvalupper(self):
        list_val =[0,11,22,109,700,809,9001, 100001]
        self.assertEqual(bin_search(109, 0, len(list_val)-1, list_val), 3 )

    def test_bin_search_not_in_list(self):
        list_val =[1,9,21,36,49,72,81,90]
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )

    def test_bin_search_one_val_list(self):
        list_val = [1]
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), None )




if __name__ == "__main__":
        unittest.main()
