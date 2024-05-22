import unittest
from merge_sort import Merge

class TestMerge(unittest.TestCase):
    def test_merge(self):
        # Test case with elements in random order
        input_data = [1, 4, 2,3, 5]
        expected_output = [1, 2, 3, 4, 5]
        Merge(input_data, 0, 1, len(input_data) - 1)
        self.assertEqual(input_data, expected_output)
        # Test case with elements in sorted order
        input_data = [1, 2,3,4, 5]
        expected_output = [1, 2, 3, 4, 5]
        Merge(input_data, 0, 2, len(input_data) - 1)
        self.assertEqual(input_data, expected_output)
        # Test case with single element
        input_data = [1]
        expected_output = [1]
        Merge(input_data, 0, 0, len(input_data) - 1)
        self.assertEqual(input_data, expected_output)

if __name__ == "__main__":
    unittest.main()
