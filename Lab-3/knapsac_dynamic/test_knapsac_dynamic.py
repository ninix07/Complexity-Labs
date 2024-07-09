import unittest
from knapsac_dynamic import find_included_items
class TestKnapsack(unittest.TestCase):
    def test_knapsack_max_value(self):
        weights = [4, 3, 2, 1, 3]
        values = [5, 2, 3, 2, 4]
        capacity = 7
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 10)
        self.assertEqual(included_items, [1, 3, 4])

        weights = []
        values = []
        capacity = 5
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 0)
        self.assertEqual(included_items, [])

        weights = [2, 3, 4]
        values = [3, 4, 5]
        capacity = 0
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 0)
        self.assertEqual(included_items, [])

        weights = [3]
        values = [10]
        capacity = 5
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 10)
        self.assertEqual(included_items, [1])

        weights = [7]
        values = [10]
        capacity = 5
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 0)
        self.assertEqual(included_items, [])

        weights = [1, 2, 3]
        values = [6, 10, 12]
        capacity = 6
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 28)
        self.assertEqual(included_items, [1, 2, 3])

        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 9)
        self.assertEqual(included_items, [2, 3])

        weights = [2, 2, 2]
        values = [10, 20, 30]
        capacity = 4
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 50)
        self.assertEqual(included_items, [2, 3])

        weights = [1, 2, 3]
        values = [10, 20, 30]
        capacity = 6
        included_items, max_value = find_included_items(weights, values, capacity)
        self.assertEqual(max_value, 60)
        self.assertEqual(included_items, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
