from typing import List
import unittest
from unittest import result
from first_contribution import Samplefunc as sa
from io import StringIO
  
class TestSamplefunc(unittest.TestCase):
      
    def setUp(self):
        pass
  
    # Returns True if the string contains 4 a.
    def test_generate_combination(self):
        obj = sa()
        result =obj.generate_combination(2, ["Amlan", "Mohit", "Kumr"])
        self.assertEqual(['Amlan Mohit', 'Amlan Kumr', 'Mohit Kumr'], result)
    
    def test_flatten_list(self):
        obj = sa()
        output = obj.flatten_list([1,2,3,["hello"],{"name","place"},[23,4,5,6,[1,2,[67,78]]]])
        result = list(output)
        self.assertListEqual([1, 2, 3, 'hello', 'place', 'name', 23, 4, 5, 6, 1, 2, 67, 78],result)
    
    def test_file_read(self):
        obj = sa()
        result = obj.file_read(r"C:\Users\Mohit Ranjan Sahoo\PycharmProjects\all_practice\pyexcel\poems.txt")
        self.assertRegex(r"My name is Mohit\n",result)

if __name__ == '__main__':
    unittest.main()
