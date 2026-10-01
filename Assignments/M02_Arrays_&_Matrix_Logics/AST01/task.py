#Task
from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    result = [[rStart, cStart]]
    r, c = rStart, cStart
    steps = 1

    while len(result) < rows * cols:
        # Move east
        for _ in range(steps):
            c += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])

        # Move south
        for _ in range(steps):
            r += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])

        steps += 1

        # Move west
        for _ in range(steps):
            c -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])

        # Move north
        for _ in range(steps):
            r -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])

        steps += 1

    return result