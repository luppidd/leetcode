from typing import List, Optional

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


    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        ans, left = 0,0

        curr =1

        for right in range(len(nums)):
            curr *= nums[right]

            while curr >= k:
                curr /= nums[left]
                left += 1

            ans += right - left +1
        return ans
    
    def findmaxAverage(self, nums: List[int], k: int) -> float:
        """ find a contigous subarray whose length is equal to k with the maximum average 
        value and return this value"""

        left, right = 0, k-1

        curr_sum = sum(nums[left:right+1])
        temp_sum = curr_sum

        while right < len(nums)-1:

            right += 1
            left += 1
            temp_sum = temp_sum + nums[right] - nums[left-1]

            if temp_sum > curr_sum:
                curr_sum = temp_sum

        return curr_sum/k

    def findMaxConsecutiveOnesI(self, nums: List[int]) -> int:   

        #Notes on this one, update your temp variables before you check if the current vlaue is bigger than the max value
        # Or at least have a think about it while you are writing it out loud.


        l, r = 0, 0
        max = 0
        curr = 0

        while r < len(nums):
            if nums[r] == 0:
                
                r +=1
                l = r
                curr = 0
                #Gotta continue here because we don't want to updtae the max value
                # if we have a zero in the array
                continue

            curr += 1
            r += 1
            if curr >max:
                max = curr

        return max
              
    def findMaxConsecutiveOnesIII(self, nums: List[int], k: int) -> int:

        left, right = 0, 0

        max = 0
        pass





if __name__ == "__main__":
    s = Solution()

    assert s.containsDuplicate([1,2,3,1]) == True
    assert s.containsDuplicate([1,2,3,4]) == False
    assert s.twoSum([2,7,11,15], 9) == (0,1)
    assert s.maxProfit1([7,1,5,3,6,4]) == 5
    assert s.isValid("()") == True  
    assert s.numSubarrayProductLessThanK([10,5,2,6], 100) == 8
    assert s.numSubarrayProductLessThanK([1,2,3], 0) == 0
    assert s.findmaxAverage([1,12,-5,-6,50,3], 4) == 12.75
    assert s.findmaxAverage([0,4,0,3,2], 1) == 4.0
    assert s.findMaxConsecutiveOnesI([1,1,0,1,1,1]) == 3

