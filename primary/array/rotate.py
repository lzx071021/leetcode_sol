from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def layer(size): return size - size // 2
        def get_new_row(old_col): return old_col
        def get_new_col(old_row): return n - old_row - 1

        for layer, layer_size in zip(range(layer(n)), range(n-1, -1, -2)):
            while layer_size > 0:
                layer_size -= 1
                old_row, old_col = layer, layer_size + layer
                pos = []
                pos.append((old_row, old_col))
                for _ in range(3):
                    new_row, new_col = get_new_row(
                        old_col), get_new_col(old_row)
                    pos.append((new_row, new_col))
                    old_row, old_col = new_row, new_col

                start_row, start_col = pos[-1]
                previous = matrix[start_row][start_col]
                for i in range(4):
                    next_row, next_col = pos[i]
                    temp = matrix[next_row][next_col]
                    matrix[next_row][next_col] = previous
                    previous = temp
        return matrix


a = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

a1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

sol = Solution()
for row in a1:
    print(row)
matrix = sol.rotate(a1)
print()
for row in matrix:
    print(row)
