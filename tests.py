import unittest
from sorting_algorithms import ExtendedList


class BubbleSortTest(unittest.TestCase):

    def setUp(self):
        self.extended_list = ExtendedList()

    """
    This tests the merge_sort method of the ExtendedList.
    """
    def test_swap(self):
        # This swaps two elements of a list using it's index.
        self.extended_list += [1, 2]
        self.assertEqual(self.extended_list.swap(0, 1), [2, 1])  # Testing to see if it actually works.

        # These test to see if an invalid index throws the correct error.
        with self.assertRaises(IndexError):
            self.extended_list.swap(0, 2)
        with self.assertRaises(IndexError):
            self.extended_list.swap(-1, 1)

    def test_bubble_sort(self):
        self.extended_list += [7, 2, 3, 8, 2, 5]

        # Checks if the sorting algorithm works.
        self.assertEqual(self.extended_list.bubble_sort(), [2, 2, 3, 5, 7, 8])


if __name__ == '__main__':
    unittest.main()
