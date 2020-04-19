"""Selection Sort Python implementation for CLRS 3/e"""


def selection_sort(A):
    n = len(A)

    # Find the first n-1 smallest element
    for j in range(n-1):
        smallest = j

        # Determine the position of the smallest element in A[j+1:n-1]
        for i in range(j+1, n):
            if A[i] < A[smallest]:
                smallest = i

        # Exchange the smallest element with A[j]
        A[j], A[smallest] = A[smallest], A[j]


if __name__ == '__main__':
    A = [2, 5, 3, 1, 6, 4]
    print(A)
    selection_sort(A)
    print(A)
