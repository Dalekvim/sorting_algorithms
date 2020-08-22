import unittest
from sorting_algorithms import ExtendedList


class MergeSortTest(unittest.TestCase):

    """
    This tests the merge_sort method of the ExtendedList.
    """
    def test_merge_sort(self):
        """This sorts the list without permanently altering it."""
        extended_list = ExtendedList()
        extended_list += [1, 2]

        self.assertEqual(extended_list.swap(), [2, 1])


if __name__ == '__main__':
    unittest.main()
