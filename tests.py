import unittest
import leetcode as leetc


class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = leetc.Solution()
        

    def test_ContainsDuplicate(self):
        self.assertEqual(self.solution.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(self.solution.containsDuplicate([1,2,3,4]), False)
    
    def test_twoSum(self):
        self.assertEqual(self.solution.twoSum([2,7,11,15], 9), (0,1))

    def test_maxProft1(self):
        self.assertEqual(self.solution.maxProfit1([7,1,5,3,6,4]), 5)
        
    def test_isValid(self):
        self.assertEqual(self.solution.isValid("()") == True)

