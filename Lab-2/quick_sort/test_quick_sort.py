import unittest
from quick_sort import quick_sort

class TestSum(unittest.TestCase):
    def test_insertion_sort(self):
        input_data= [3,4,2]
        result= quick_sort(input_data,0, len(input_data)-1)
        self.assertEqual(result,[2,3,4])

        input_data=[]
        result= quick_sort(input_data, 0, len(input_data)-1)
        self.assertEqual(result,[])
        
        input_data=[2,4,7,8,3,1]
        result= quick_sort(input_data, 0, len(input_data)-1)
        self.assertEqual(result,[1,2,3,4,7,8])

if __name__ =="__main__":
    unittest.main()