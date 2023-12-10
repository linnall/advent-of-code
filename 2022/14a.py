def drop_sand(grid, maxCol, maxRow):
    currCoor = (500, 0)
    sandCount = 0
    while True:
        # print(currCoor)
        col, row = currCoor
        if row + 1 > maxRow:
            return sandCount
        if grid[row + 1][col] == '.':
            currCoor = (col, row + 1)
            continue
        if col - 1 < 0:
            return sandCount
        if grid[row + 1][col - 1] == '.':
           currCoor = (col - 1, row + 1)
           continue
        if col + 1 > maxCol:
            return sandCount
        if grid[row + 1][col + 1] == '.':
            currCoor = (col + 1, row + 1)
            continue
        # sand cannot fall further
        grid[row][col] = '+'
        currCoor = (500, 0)
        sandCount += 1
        continue

def solution():
    maxRow = 0
    maxCol = 500
    with open('14.in', 'r') as file:
        lines = file.read().split('\n')
        walls = []
        for line in lines:
            coordinates = line.split(' -> ')
            startCoor = list(map(int, coordinates[0].split(',')))
            maxCol = max(maxCol, startCoor[0])
            maxRow = max(maxRow, startCoor[1]) 
            for coor in coordinates[1:]:
                endX, endY = list(map(int, coor.split(',')))
                maxCol = max(maxCol, endX)
                maxRow = max(maxRow, endY)
                walls.append([startCoor, [endX, endY]])
                startCoor = [endX, endY]
    grid = [['.' for _ in range(maxCol + 1)] for _ in range(maxRow + 1)]

    # adding walls
    for wall in walls:
        start, end = wall
        startX, startY = start
        endX, endY = end
        if startX != endX:
            left = min(startX, endX)
            for i in range(abs(startX - endX) + 1):
                grid[startY][left + i] = '#'
        else: # startY != endY
            left = min(startY, endY)
            for i in range(abs(startY - endY) + 1):
                grid[left + i][startX] = '#'

    return drop_sand(grid, maxCol, maxRow)

print(solution())