"""Bubble Sort Python implementation for CLRS 3/e"""


def bubble_sort(A):
    n = len(A)

    # Starting from the first element, each iteration of the outer loop "bubbles" the smallest element in the unsorted subarray A[i+1:n] to the end of the sorted subarray.
    for i in range(n-1):
        # Using reversed(range()) is more elegant than using pure range() when iterating in reversed order.
        for j in reversed(range(i+1, n)):
            # "Bubble": exchanging a pair of elements to move backward one step a time.
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


if __name__ == '__main__':
    A = [2, 5, 3, 1, 6, 4]
    print(A)
    bubble_sort(A)
    print(A)
