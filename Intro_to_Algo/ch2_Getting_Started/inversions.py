"""Count Inversions Python implementation for CLRS 3/e"""


from math import floor


def count_inversions(A, p, r):
    inversions = 0
    if p < r:
        q = floor((p+r)/2)
        inversions += count_inversions(A, p, q)
        inversions += count_inversions(A, q+1, r)
        inversions += merge_inversions(A, p, q, r)
    return inversions


def merge_inversions(A, p, q, r):
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
    inversions = 0
    counted = False
    for k in range(p, r+1):
        if not counted and R[j] < L[i]:
            inversions += n1 - i
            counted = True
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
            counted = False
    return inversions


if __name__ == '__main__':
    A = [2, 5, 3, 1, 6, 4]
    print(count_inversions(A, 0, len(A)-1))
    A = [2, 3, 8, 6, 1]
    print(count_inversions(A, 0, len(A)-1))
