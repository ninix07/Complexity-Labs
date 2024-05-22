import unittest
from quick_sort import partition

class TestPartition(unittest.TestCase):
    def test_partition(self):
        # Test case with elements in random order
        input_data = [3, 4, 2, 1, 5]
        pivot_index = partition(input_data, 0, len(input_data) - 1)
        self.assertEqual(pivot_index, 4) 
        self.assertTrue(all(input_data[i] <= input_data[pivot_index] for i in range(pivot_index)))
        self.assertTrue(all(input_data[i] > input_data[pivot_index] for i in range(pivot_index + 1, len(input_data))))

        # Test case with elements already sorted
        input_data = [1, 2, 3, 4, 5]
        pivot_index = partition(input_data, 0, len(input_data) - 1)
        self.assertEqual(pivot_index, 4)  
        self.assertTrue(all(input_data[i] <= input_data[pivot_index] for i in range(pivot_index)))
        self.assertTrue(all(input_data[i] > input_data[pivot_index] for i in range(pivot_index + 1, len(input_data))))



if __name__ == "__main__":
    unittest.main()