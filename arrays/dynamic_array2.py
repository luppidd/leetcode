"""I wrote this one to see how close I could get to the first verison I wrote using a textbook"""


from types import *
import ctypes

class DynamicArray:

    def __init__(self):
        """ Create an empty array"""
        self._n : int = 0
        self._capacity : int = 1
        self._A = self._make_array(self._capacity)

    def __repr__(self) -> str:
        return "Array n: %s, capacity: %s" % (self._n, self._capacity)

    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        #I made a mistake here, I had <= self._n which allowed me to call
        # indexes that were out of range.
        if not 0 <= k < self._n:
            raise IndexError("This index is invalid")
        return self._A[k]
    
    def _make_array(self, c):
        return (c*ctypes.py_object)()
    
    def _resize(self, c):
        """Allows upsizing and downsizing in the future"""
        B = self._make_array(c*2)
        for k in range(self._n):
            B[k] = self._A[k]

        # Made Correction here, forgot to increase the capacity of the dynamic array
        self._capacity = c*2
        self._A = B

        return self._A
    
    def append(self, obj):
        """ This method depends on a function to resize"""
        
        if self._n == self._capacity:
            """Default double array size for appending"""
            self._resize(self._n*2)
        
        self._A[self._n] = obj
        self._n += 1 

        return self._A

        
if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(len(arr))
    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr._capacity)
    print(arr[3])