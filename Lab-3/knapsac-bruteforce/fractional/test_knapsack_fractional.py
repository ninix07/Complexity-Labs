import unittest
from knapsack_fractional import knapsack_fractional

class TestKnapsackFractional(unittest.TestCase):
    def test_knapsack_fractional(self):

        weights = [2, 2, 3]
        profits = [6, 10, 12]
        capacity = 6
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [0.5, 1, 1])


        weights = []
        profits = []
        capacity = 5
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [])


        weights = [2, 3, 4]
        profits = [3, 4, 5]
        capacity = 0
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [0, 0, 0])


        weights = [3]
        profits = [10]
        capacity = 5
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [1.0])


        weights = [7]
        profits = [10]
        capacity = 5
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [5/7])

        weights = [1, 2, 3]
        profits = [6, 10, 12]
        capacity = 6
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [1.0, 1.0, 1.0])

        weights = [2, 2, 2]
        profits = [10, 20, 30]
        capacity = 5
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [0.5, 1.0, 1.0])

        weights = [1, 3, 4, 5]
        profits = [1, 4, 5, 7]
        capacity = 7
        result,  _ ,_= knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [0, 2/3, 0, 1])


        weights = [1, 2, 3]
        profits = [10, 20, 30]
        capacity = 6
        result, _, _ = knapsack_fractional(weights, profits, capacity)
        self.assertEqual(result, [1.0, 1.0, 1.0])


if __name__ == "__main__":
    unittest.main()
