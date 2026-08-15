'''54. Spiral Matrix'''
from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:

    if not matrix or not matrix[0]:
        return []

    result = []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Top to bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Right to left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Bottom to top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))


'''59. Spiral Matrix II'''
def generateMatrix(n: int) -> List[List[int]]:

    matrix = [[0] * n for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while top <= bottom and left <= right:

        # Left to right
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Top to bottom
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # Right to left
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
        bottom -= 1

        # Bottom to top
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = num
            num += 1
        left += 1

    return matrix
n = 3
print(generateMatrix(n))

