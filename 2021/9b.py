from collections import deque

def inMatrix(coor, r, c):
    row, col = coor
    if row < 0 or row > r - 1 or col < 0 or col > c - 1:
        return False
    return True


def solution():
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

    basins = []

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
            basins.append((i, j))

    # track 3 largest basins
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    basinSizes = []
    for basin in basins:
        queue = deque([basin])
        size = 0
        seen = set()
        while queue:
            row, col = queue.popleft()
            if (row, col) in seen:
                continue
            size += 1
            seen.add((row, col))
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if inMatrix([newRow, newCol], n, m) and int(matrix[newRow][newCol]) > int(matrix[row][col]) and matrix[newRow][newCol] != '9':
                    queue.append((newRow, newCol))
        basinSizes.append(size)
    basinSizes.sort(reverse=True)
    return basinSizes[0] * basinSizes[1] * basinSizes[2]


print(solution())
