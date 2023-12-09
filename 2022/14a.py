def drop_sand(grid, maxX, maxY):
    # row, col
    currCoor = (0, 500)
    sandCount = 0
    prevCoor = (0, 500)
    while True:
        # row, col
        x, y = currCoor
        print(y, x)
        if grid[x][y] == '#':
            grid[prevCoor[0]][prevCoor[1]] = '+' # sand lands
            sandCount += 1
            currCoor = (0, 500)
            prevCoor = (0, 500)
            continue
        # if x < 0 or x > maxX or y < 0 or y > maxY:
        #     return sandCount
        if x + 1 > maxY:
            return sandCount
        if grid[x + 1][y] == '.':
            prevCoor = currCoor
            currCoor = (x + 1, y)
            continue
        if y - 1 < 0:
            return sandCount
        if grid[x + 1][y - 1] == '.':
            prevCoor = currCoor
            currCoor = (x + 1, y - 1)
            continue
        if y + 1 > maxX:
            return sandCount
        if grid[x + 1][y + 1] == '.':
            prevCoor = currCoor
            currCoor = (x + 1, y + 1)
            continue


def solution():
    maxX = 500
    maxY = 0
    with open('14.in', 'r') as file:
        lines = file.read().split('\n')
        walls = []
        for line in lines:
            coordinates = line.split(' -> ')
            startCoor = list(map(int, coordinates[0].split(',')))
            for coor in coordinates[1:]:
                endX, endY = list(map(int, coor.split(',')))
                maxX = max(maxX, endX)
                maxY = max(maxY, endY)
                walls.append([startCoor, [endX, endY]])
                startCoor = [endX, endY]
    grid = [['.' for _ in range(maxX + 1)] for _ in range(maxY + 1)]
    # adding walls
    for wall in walls:
        start, end = wall
        startX, startY = start
        endX, endY = end
        if startX != endX:
            for i in range(startX, endX + 1):
                grid[startY][i] = '#'
        else:
            for i in range(startY, endY + 1):
                grid[i][startX] = '#'
    
    return drop_sand(grid, maxY, maxX)

print(solution())