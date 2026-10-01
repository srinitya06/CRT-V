from typing import List

def diagonalBoundarySum(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                total += arr[i][j]
            elif i == j or i + j == n - 1:
                total += arr[i][j]

    return total