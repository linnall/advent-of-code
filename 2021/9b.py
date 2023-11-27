'''
using where the low points are, dfs on all neighbors of low point
condition: current square must be strictly increasing 
edge case: the next square has the SAME height as the current square -> -1 from size of basin
'''
import heapq

# maintain this heap as size 3
largestBasins = []
heapq.heapify(largestBasins)

def inMatrix(coor, r, c):
    row, col = coor
    if row < 0 or row > r - 1 or col < 0 or col > c - 1:
        return False
    return True

def dfs(matrix, n, m, coor):
    i, j = coor
    val = int(matrix[i][j])
    
    # if square has already been visited, return
    if val == 10:
        return 1

    # mark as visited
    matrix[i][j] = "10"

    # check if top, left, right, left are strictly increasing
    # top
    if inMatrix([i - 1, j], n, m):
        if int(matrix[i-1][j]) == 9 or int(matrix[i-1][j]) <= val:
            return 1
        else:
            return dfs(matrix, n, m, [i - 1, j]) + 1
    # bottom
    if inMatrix([i + 1, j], n, m) or int(matrix[i-1][j]) <= val:
        if int(matrix[i+1][j]) == 9:
            return 1
        else:
            return dfs(matrix, n, m, [i + 1, j]) + 1
    # left
    if inMatrix([i, j - 1], n, m) or int(matrix[i-1][j]) <= val:
        if int(matrix[i][j-1]) == 9:
            return 1
        else:
            return dfs(matrix, n, m, [i, j - 1]) + 1      

    # right
    if inMatrix([i, j + 1], n, m) or int(matrix[i-1][j]) <= val:
        if int(matrix[i][j+1]) == 9:
            return 1
        else:
            return dfs(matrix, n, m, [i, j + 1]) + 1



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

    for i in range(n):
        for j in range(m):
            val = int(matrix[i][j])

            # part of a basin, cannot be a low point
            if val == 10:
                continue

            # top
            if inMatrix([i - 1, j], n, m):
                if int(matrix[i-1][j]) <= val or int(matrix[i-1][j]) == 10:
                    continue
            # bottom
            if inMatrix([i + 1, j], n, m):
                if int(matrix[i+1][j]) <= val or int(matrix[i-1][j]) == 10:
                    continue
            # left
            if inMatrix([i, j - 1], n, m):
                if int(matrix[i][j-1]) <= val or int(matrix[i-1][j]) == 10:
                    continue
            # right
            if inMatrix([i, j + 1], n, m):
                if int(matrix[i][j+1]) <= val or int(matrix[i-1][j]) == 10:
                    continue

            print("value of lowest point:")
            print(val)
            # current cell in matrix is a low point
            basinSize = dfs(matrix, n, m, [i, j])
            print("basin size: ")
            print(basinSize)
            if not largestBasins or basinSize > largestBasins[0]:
                if largestBasins:
                    heapq.heappop(largestBasins)
                heapq.heappush(largestBasins, basinSize)
    
    # multiply largest basin sizes
    product = 1
    for basin in largestBasins:
        product *= basin

solution()
