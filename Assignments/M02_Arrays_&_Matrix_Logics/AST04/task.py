def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    for start_col in range(cols):
        diagonal = []
        r, c = 0, start_col

        while r < rows and c < cols:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r, c = 0, start_col
        i = 0
        while r < rows and c < cols:
            mat[r][c] = diagonal[i]
            i += 1
            r += 1
            c += 1

    for start_row in range(1, rows):
        diagonal = []
        r, c = start_row, 0

        while r < rows and c < cols:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r, c = start_row, 0
        i = 0
        while r < rows and c < cols:
            mat[r][c] = diagonal[i]
            i += 1
            r += 1
            c += 1

    return mat