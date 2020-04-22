"""Linear Search implementation for CLRS 3/e"""


def linear_search(A, value):
    # * Python has a more elegant implementation using enumerate().
    for i in range(len(A)):
        if value == A[i]:
            # Return the index of the first entry that is equal to the searching value.
            return i
    # Rather than returning None(or NIL), we return -1 as the non-exist index to indicate that the value is not in the array A.
    return -1


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    print(linear_search(A, 3))
