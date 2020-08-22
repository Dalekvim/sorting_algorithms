import unittest
from sorting_algorithms import ExtendedList


class MergeSortTest(unittest.TestCase):

    """
    This tests the merge_sort method of the ExtendedList.
    """
    def test_swap(self):
        """This sorts the list without permanently altering it."""
        extended_list = ExtendedList()
        extended_list += [1, 2]

        self.assertEqual(extended_list.swap(0, 1), [2, 1])

        with self.assertRaises(IndexError):
            extended_list.swap(0, 2)

        with self.assertRaises(IndexError):
            extended_list.swap(-1, 1)


if __name__ == '__main__':
    unittest.main()
