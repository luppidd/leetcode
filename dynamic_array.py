from typing import *
import ctypes


class DynamicArray:

    def __init__(self, capacity: int):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def _resize(self, c):
        """resize internal array to capacity c"""
        # Initialize a new array to replace A
        B = self._make_array(c)
        # Fill the new array for each k in A
        for k in range(self._n):
            B[k] = self._A[k]

        # replace A
        self._A = B
        # update capcity with c
        self._capacity = c

    def append(self, obj):
        """Add an object to the end of the array"""

        # check if the array is at capacity, if so double
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        # add object at last index end and increase the len count
        self._A[self._n] = obj
        self._n += 1

if __name__ == "__main__":
    arr = DynamicArray(1)
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(len(arr))
    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr._capacity)
    print(arr[3])
