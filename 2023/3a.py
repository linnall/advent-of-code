def solution():
    with open('3.in', 'r') as file:
        lines = file.read().split('\n')
        N = len(lines)
        M = len(lines[0])
        grid = [['' for _ in range(M)] for _ in range(N)]
        numbers_pos = []
        for i, line in enumerate(lines):
            num = ''
            for j, ch in enumerate(line):
                if ch.isnumeric():
                    num += ch
                elif ch != '.':
                    grid[i][j] = ch

                if not ch.isnumeric() and num:
                    numbers = []
                    for k, digit in enumerate(num):
                        newCol = j - len(num) + k
                        grid[i][newCol] = num
                        numbers.append((i, newCol))
                    numbers_pos.append(numbers)
                    num = ''
            if num:
                numbers = []
                for k, digit in enumerate(num):
                    newCol = M - len(num) + k
                    grid[i][newCol] = num
                    numbers.append((i, newCol))
                numbers_pos.append(numbers)
                num = ''
        # check adjacency for each special char
        total = 0
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        for l in numbers_pos:
            for i, j in l:
                isPart = False
                for row, col in direction:
                    newRow = i + row
                    newCol = j + col
                    if newRow >= 0 and newRow < N and newCol >= 0 and newCol < M and grid[newRow][newCol] and not grid[newRow][newCol].isnumeric():
                        isPart = True
                        break
                if isPart:
                    total += int(grid[i][j])
                    isPart = False
                    break
        return total

print(solution())