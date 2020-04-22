"""Insertion Sort Python implementation for CLRS 3/e"""


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i + 1] = key


if __name__ == '__main__':
    A = [2, 5, 3, 1, 6, 4]
    print(A)
    insertion_sort(A)
    print(A)
