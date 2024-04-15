from typing import List, Any


def insertion_sort(A: List[Any]) -> list[Any]:
    """ Pseudo
    Sort a list of comparable elements into non decreasing order
    
    for k from 1 to n-1:
        insert A[k] at it's proper location in A
    """

    for k in range(len(A)):
        # we keep track of current so we can put it in the right spot
        # at the end of the iteration when we've found it's position
        current = A[k]
        j = k

        #Sarch for the right position of k in A while moving elements
        # that are greateer rightwards
        while j > 0 and A[j-1]>current:
            A[j] = A[j-1]
            j -=1
        A[j] = current
    
    return A

if __name__ == '__main__':
    print(insertion_sort([3,2,1]))
    assert insertion_sort([3,2,1]) == [1,2,3]