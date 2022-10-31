def inMatrix(coor, r, c):
    row, col = coor
    if row < 0 or row > r - 1 or col < 0 or col > c - 1:
        return False
    return True


def solution():
    totalRisk = 0
    matrix = []
    with open('9.in', 'r') as file:
        for line in file:
            row = [char for char in line]
            rowLen = len(row)
            if row[rowLen - 1] == "\n":
                row.pop()
            matrix.append(row)
    # check neighbors for each cell
    n = len(matrix)
    m = len(matrix[0])
    print(matrix)

    for i in range(n):
        for j in range(m):
            val = int(matrix[i][j])

            # top
            if inMatrix([i - 1, j], n, m):
                if int(matrix[i-1][j]) <= val:
                    continue
            # bottom
            if inMatrix([i + 1, j], n, m):
                if int(matrix[i+1][j]) <= val:
                    continue
            # left
            if inMatrix([i, j - 1], n, m):
                if int(matrix[i][j-1]) <= val:
                    continue
            # right
            if inMatrix([i, j + 1], n, m):
                if int(matrix[i][j+1]) <= val:
                    continue
            totalRisk = totalRisk + val + 1

    print(totalRisk)


solution()
