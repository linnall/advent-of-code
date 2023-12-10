'''
- loop over and add 1 to each cell
    - check if value > 9, apply increasing energy level of adjacent optopi by 1 recursively
- loop over grid and mark all values > 9 to 0
'''

def inGrid(r, c):
    if r < 0 or r > 9 or c < 0 or c > 9:
        return False
    return True

def increaseEnergy(i, j, grid, seen):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    if grid[i][j] > 9 and (i, j) not in seen:
        seen.add((i, j)) # once an octopus has flashed, we don't want it flash again
        for x, y in directions:
            newRow = i + x
            newCol = j + y
            if inGrid(newRow, newCol):
                grid[newRow][newCol] += 1
                increaseEnergy(newRow, newCol, grid, seen)

def step(grid) -> int:
    flashCount = 0
    seen = set()
    # increase energy level of all octopi
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1
            if grid[i][j] > 9:
                # if octopi flashes, increase neighbors' energy
                increaseEnergy(i, j, grid, seen)
    # mark all octopi that have flashed
    for i in range(10):
        for j in range(10):
            if grid[i][j] > 9:
                grid[i][j] = 0
                flashCount += 1
    return flashCount


def solution():
    flashCount = 0
    grid = []
    with open('11.in', 'r') as file:
        lines = file.read().split('\n')
        grid = [[int(num) for num in line] for line in lines]
    
    # simulate 100 steps
    for i in range(100):
        flashCount += step(grid)

    return flashCount
    
print(solution())
        