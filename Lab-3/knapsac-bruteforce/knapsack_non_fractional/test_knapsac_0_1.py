import unittest
from knapsac_non_fractional import knapsack_non_fractional

class TestKnapsackNonFractional(unittest.TestCase):
    def test_knapsack_non_fractional(self):
        weights = [2, 1, 1, 1]
        profits = [3, 4, 5, 6]
        capacity = 5
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [1, 1, 1, 1])  


        weights = []
        profits = []
        capacity = 5
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [])

 
        weights = [2, 3, 4]
        profits = [3, 4, 5]
        capacity = 0
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [])

  
        weights = [3]
        profits = [10]
        capacity = 5
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [1])

     
        weights = [7]
        profits = [10]
        capacity = 5
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [])

    
        weights = [1, 2, 3]
        profits = [6, 10, 12]
        capacity = 6
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [1, 1, 1])

       
        weights = [1, 3, 4, 5]
        profits = [1, 4, 5, 7]
        capacity = 7
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [0, 1, 1, 0]) 

        
        weights = [2, 2, 2]
        profits = [10, 20, 30]
        capacity = 4
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [0, 1, 1])  

       
        weights = [1, 2, 3]
        profits = [10, 20, 30]
        capacity = 6
        result = knapsack_non_fractional(weights, profits, capacity)
        self.assertEqual(result, [1, 1, 1])  

if __name__ == "__main__":
    unittest.main()
