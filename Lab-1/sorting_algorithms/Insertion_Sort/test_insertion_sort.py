import unittest
from insertion_sort import insertion_sort

class TestSum(unittest.TestCase):
    def test_insertion_sort(self):
        input_data= [3,4,2]
        result= insertion_sort(input_data)
        self.assertEqual(result,[2,3,4])

        input_data=[]
        result= insertion_sort(input_data)
        self.assertEqual(result,[])

if __name__ =="__main__":
    unittest.main()