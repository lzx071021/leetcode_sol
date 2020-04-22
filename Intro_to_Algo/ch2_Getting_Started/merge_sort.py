"""Merge Sort Python implementation for CLRS 3/e"""
from math import floor


def merge_sort(A, p, r):
    if p < r:
        # Divide: compute the middle index of the subarray
        q = floor((p+r)/2)

        # Conquer
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)

        # Combine
        merge(A, p, q, r)


def merge(A, p, q, r):
    # Compute the lengths of the two new subarrays
    n1 = q - p + 1
    n2 = r - (q + 1) + 1

    # Initiate the two new subarrays with a sentinel added to each subarray
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy the elements in A to L and R
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+1+j]

    # Use infinity as the sentinel value to simplify the code
    L[n1] = float('inf')
    R[n2] = float('inf')

    # Set the cursors to the start of the new subarrays
    i = 0
    j = 0

    # Replace one element of A at each iteration using either the element from L or R.
    # The for loop exactly processes r-p+1 iterations, and with the aid of the sentinels, we don't need to check whether there're remaining elements in subarrays, neither do we check whether we're indexing out of range.
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def merge_sort_without_sentinel(A):
    # * If not in place, you need to return results of every procedure.
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    L = merge_sort_without_sentinel(A[:mid])
    R = merge_sort_without_sentinel(A[mid:])
    return merge_without_sentinel(L, R)


def merge_without_sentinel(L, R):
    res = []
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    res += L[i:]
    res += R[j:]
    return res


if __name__ == '__main__':
    A = [2, 5, 3, 1, 6, 4]
    print(A)
    merge_sort(A, 0, len(A)-1)
    print(A)

    print('Without sentinels:')
    A = [2, 5, 3, 1, 6, 4]
    print(A)
    print(merge_sort_without_sentinel(A))
