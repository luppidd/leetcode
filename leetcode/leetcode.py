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
        # Leetcode 125
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
        # Leetcode 20
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
        # Leetcode 206
        
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
        # leetcode 713
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
        # Leetcode 643
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
        # Leetcode 485
        l, r = 0, 0
        max = 0
        l = 0

        while r < len(nums):
            if nums[r] == 0:
                
                r +=1
                l = r

                continue

            r += 1
            curr = r - l 
            if (curr) >max:
                max = curr

        return max
              
    def findMaxConsecutiveOnesIII(self, nums: List[int], k: int) -> int:
        # Leetcode 1004
        left = 0

        for right in range(len(nums)):


            k -= 1 -nums[right]

            if k < 0:
                k+= 1 - nums[left]
                left += 1

        return (right - left + 1)
    
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    def minStartValue(self, nums: List[int]) -> int:
    
        prefix = nums[0]
        min_ = prefix
        for i in range(1, len(nums)):
            prefix += nums[i]
            min_ = min(min_, prefix)
        
        if min_>= 1:
            return 1
        
        else:
            return 1- min_
        
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        avg = []

        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[i-1])
            
        for i in range(len(prefix)):
            if i+k > len(prefix)-1 or i-k < 0:
                avg.append(-1)
                
            else:
                avg.append((prefix[i+k]-prefix[i-k]+nums[i-k])//(2*k+1))
        
        return avg

    def repeatedCharacter(self, s:str) -> str:
        """ Leetcode 2351, This returns the first character to apper
        twice using brute force"""

        for i in range(len(s)):
            c = s[i]
            for j in range(i):
                if s[j] == c:
                    return c
    
    def repeatedCharacter2(self, s:str) -> str:
        """ Leetcode 2351, This returns the first character to apper
        twice using a dict, space complexity is equal to O(m) which is 
        the allowable number of characters in s. It can also be argued that the solution 
        runs in O(1) cause it's bounded by 26, the number of allowable characters in the
        english alphabet"""


        d = {}
        for i in range(len(s)):
            c = s[i]
            if c in d:
                return c
            d[c] = i

    def checkIfPangram(self, sentence: str) -> bool:
        """ Leetcode 1832. Check if pangram, solved using a set. This solution is O(n) but space complexity is O(1)"""

        set_sentence= set(sentence)
        if len(set_sentence) == 26:
            return True
        return False