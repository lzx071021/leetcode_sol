"""Binary Search Python implementation for CLRS 3/e"""


from math import floor
from bubble_sort import bubble_sort


def recursive_binary_search(A, value, low, high):
    """The array A must be sorted beforehand!"""
    # Notice the condition to terminating the recursion of recursive one is different to that of iterative one.
    if low > high:
        return -1
    mid = floor((low+high)/2)
    if value == A[mid]:
        return mid
    elif value > A[mid]:
        return recursive_binary_search(A, value, mid+1, high)
    else:
        return recursive_binary_search(A, value, low, mid-1)
    # Notice we don't need to add a return statement here, because every case is handled by the if statements listed above.
    # return -1


def iterative_binary_search(A, value, low, high):
    """The array A must be sorted beforehand!"""
    # Notice that here we have to put "<=" to accommodate the case such that there's only a single entry in the array A.
    while low <= high:
        mid = floor((low+high)/2)
        if value == A[mid]:
            return mid
        elif value > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    A = [2, 5, 3, 1, 6, 4]
    value = 5
    bubble_sort(A)
    print(recursive_binary_search(A, value, 0, len(A)-1))
    print(iterative_binary_search(A, value, 0, len(A)-1))
