'''
"I pledge my honor that I have abided by the Stevens Honor System" ncolonna

Created on Sep 30, 2017

@author: Colonna
'''
import unittest
import hw4

class Test(unittest.TestCase):
    
    def test01(self):
        self.assertEqual(hw4.pascal_row(0), [1])
        self.assertEqual(hw4.pascal_row(1), [1, 1])
        self.assertEqual(hw4.pascal_row(2), [1, 2, 1])
        self.assertEqual(hw4.pascal_row(3), [1, 3, 3, 1])
        self.assertEqual(hw4.pascal_row(5), [1, 5, 10, 10, 5, 1])


    def test02(self):
        self.assertEqual(hw4.pascal_triangle(0), [[1]])
        self.assertEqual(hw4.pascal_triangle(1), [[1], [1, 1]])
        self.assertEqual(hw4.pascal_triangle(2), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(hw4.pascal_triangle(3), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        self.assertEqual(hw4.pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])

if __name__ == "__main__": 
    unittest.main()