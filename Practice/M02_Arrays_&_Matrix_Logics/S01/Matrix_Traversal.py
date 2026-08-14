'''1572. Matrix Diagonal Sum'''
from typing import List

def diagonalSum(self, mat: List[List[int]]) -> int:
    n = len(mat)
    s = 0

    for i in range(n):
        s += mat[i][i]
        s += mat[i][n - i - 1]

    if n % 2 == 1:
        s -= mat[n // 2][n // 2]

    return s
mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
print(diagonalSum(0, mat))
'''498. Diagonal Traverse'''
def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    rows, cols = len(mat), len(mat[0])
    res = []

    for d in range(rows + cols - 1):
        diagonal = []

        r = 0 if d < cols else d - cols + 1
        c = d if d < cols else cols - 1

        while r < rows and c >= 0:
            diagonal.append(mat[r][c])
            r += 1
            c -= 1

        if d % 2 == 0:
            diagonal.reverse()

        res += diagonal

    return res
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(0, mat))