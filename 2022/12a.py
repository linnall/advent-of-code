from collections import deque


def print_grid(grid):
    lines = []
    for line in grid:
        s = "".join(line)
        lines.append(s)
        lines.append("\n")
    print("".join(lines))


def bfs(grid, start, end):
    seen = set()
    queue = deque([start])
    pathLen = 0
    levelNum = len(queue)
    while queue:
        # print(queue)
        row, col = queue.popleft()
        levelNum -= 1
        if row == end[0] and col == end[1]:
            return pathLen
        if (row, col) in seen:
            if levelNum == 0:
                levelNum = len(queue)
                pathLen += 1
            continue
        seen.add((row, col))
        # if grid[row][col] == ".":
        #     continue
        # try neighbors
        currElevation = ord(grid[row][col])
        if row > 0:
            if currElevation + 1 >= ord(grid[row - 1][col]):
                queue.append([row - 1, col])
            # else:
            #     grid[row - 1][col] = "."
        if row < len(grid) - 1:
            if currElevation + 1 >= ord(grid[row + 1][col]):
                queue.append([row + 1, col])
            # else:
            #     grid[row + 1][col] = "."
        if col > 0:
            if currElevation + 1 >= ord(grid[row][col - 1]):
                queue.append([row, col - 1])
            # else:
            #     grid[row][col - 1] = "."
        if col < len(grid[0]) - 1:
            if currElevation + 1 >= ord(grid[row][col + 1]):
                queue.append([row, col + 1])
            # else:
            #     grid[row][col + 1] = "."
        grid[row][col] = "."  # mark current cell as visited
        if levelNum == 0:
            levelNum = len(queue)
            pathLen += 1


def solution():
    with open("12.in", "r") as file:
        lines = file.read().split("\n")
        grid = [list(line) for line in lines]

    start = [0, 0]
    end = [0, 0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = [i, j]
                grid[i][j] = "a"
            elif grid[i][j] == "E":
                end = [i, j]
                grid[i][j] = "z"

    # run bfs
    return bfs(grid, start, end)


print(solution())
