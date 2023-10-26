def isSeen(height, grid, tree, direction):
    row, col = tree
    if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
        return True
    if grid[row][col] < height:
        return isSeen(height, grid, (row + direction[0], col + direction[1]), direction)
    else:
        return False


def solution():
    with open("8.in", "r") as file:
        lines = file.read().split("\n")
        grid = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for line in lines:
            row = list(map(int, list(line)))
            grid.append(row)
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for direction in directions:
                    if isSeen(
                        grid[i][j],
                        grid,
                        (i + direction[0], j + direction[1]),
                        direction,
                    ):
                        count += 1
                        print(i, j)
                        break

        return count


print(solution())
