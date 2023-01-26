from collections import deque
from typing import List

OFFSETS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
inf = float("inf")


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """Dynamic programming solution, memory is O(1)"""
        rows, cols = len(mat), len(mat[0])

        for r in range(rows):
            for c in range(cols):
                top = mat[r - 1][c] if r - 1 > 0 else inf
                left = mat[r][c - 1] if c - 1 > 0 else inf
                mat[r][c] = min(top + 1, left + 1, mat[r][c])

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                bottom = mat[r + 1][c] if r + 1 < rows else inf
                right = mat[r][c + 1] if c + 1 < cols else inf
                mat[r][c] = min(bottom + 1, right + 1, mat[r][c])

        return mat

    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        """BFS Solution starting on zero-cells"""
        rows, cols = len(mat), len(mat[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = None

        while q:
            row, col = q.popleft()

            for i, j in OFFSETS:
                orow, ocol = row + i, col + j
                if (
                    (0 <= orow < rows)  # boundary check - rows
                    and (0 <= ocol < cols)  # boundary check - columns
                    and (mat[orow][ocol] is None)  # check if visited before
                ):
                    mat[orow][ocol] = mat[row][col] + 1
                    q.append((orow, ocol))
        return mat
