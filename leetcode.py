from typing import *

class ListNode:
    def __init__(self, val=0, next=None, _list = []):
        self.val = val
        self.next = next

    def __repr__(self):
        return "val: %r" % (self.__dict__)

def list_to_listNode(list1):

    head = ListNode(list1[0])
    tail = head
    i = 1

    while i < len(list1):
        tail.next = ListNode(list1[i]) 
        tail = tail.next
        i += 1
    return head
    

class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        return len(set(nums)) != len(nums)


    def isAnagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while len(nums) > 1:
            diff = target - nums.pop()
            for i, k in enumerate(nums):
                if diff == k:
                    return i, len(nums)

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [ d[diff], i ]
            d[n] = i

    def isPalindrome(self, s:str) -> bool:
        """ This function checks a string to see if it is a palindrome.
        it also ignores alpha-numeric characters and case. it uses a two pointer solution"""
        """ is there a function that uses chars?"""
        s = [c.lower() for c in s if c.isalnum()]

        l = 0
        r = len(s) -1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True 



    def maxProfit1(self, prices: List[int]) -> int:
        """ This function is supposed to take a list of prices and return the maximum profit that can be made from buying and selling the stock.
        This is a two pointer solution that's kinda fun we start by looking at the first two prices of the list and we move the beginning to the second pointer if the second pointer is less than the first pointer then we found a new local minumum.

        We then replace pointer 1 with pointer two position.
        If this is not the case we check whether the difference between the values at the two pointer locations is greater than our max. If this is the case, we replace our max with a new maximum. 

        The last condition we just move our pointer to the right.
        """
            
        left = 0
        right = 1
        max = 0

        while right <= len(prices)-1:
            if prices[right] < prices[left]:
                left = right
                right +=1

            elif (prices[right]-prices[left])>max:
                max = prices[right]-prices[left]
                right +=1
            else:
                right +=1
        return max 
            
    def isValid(self, s: str) -> bool:
        """ This function checks for valid parentheses """

        left = '[{('
        right = ']})'

        stack = []
        
        #using a list as a stack

        for c in s:
            if c in left:
                stack += c
            if c in right:
                # if there are no characters in stack then the right closer is invalid

                if stack == []:
                    return False
                
                # If the left character index does not match the right character index 
                #  then the right closing character does not line up 
                if right.index(c) != left.index(stack.pop()):
                    return False
        return stack == []

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ This function reverses a linked list
            What could we do? We could use recursion with the lowest note returning 
            val next. We could also use two pointers to reverse the list
        """
        curr = head
        prev = None

        while curr:
            tail = curr.next
            curr.next = prev
            prev = curr
            curr = tail
        return prev

if __name__ == "__main__":
    s = Solution()

    assert s.containsDuplicate([1,2,3,1]) == True
    assert s.containsDuplicate([1,2,3,4]) == False
    assert s.twoSum([2,7,11,15], 9) == (0,1)
    assert s.maxProfit1([7,1,5,3,6,4]) == 5
    assert s.isValid("()") == True  
    s.reverseList(list_to_listNode([1,2,3,4,5])) 
