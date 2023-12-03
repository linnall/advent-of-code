def solution():
    with open('3.in', 'r') as file:
        lines = file.read().split('\n')
        N = len(lines)
        M = len(lines[0])
        grid = [['' for _ in range(M)] for _ in range(N)]
        gear_pos = []
        for i, line in enumerate(lines):
            num = ''
            for j, ch in enumerate(line):
                if ch.isnumeric():
                    num += ch
                elif ch == '*':
                    grid[i][j] = ch
                    gear_pos.append((i, j))

                if not ch.isnumeric() and num:
                    num_pos = [(i, col) for col in range(j - len(num), j)]
                    for k, digit in enumerate(num):
                        newCol = j - len(num) + k
                        grid[i][newCol] = [num, num_pos]
                    num = ''
            if num:
                num_pos = [(i, col) for col in range(M - len(num), M)]
                for k, digit in enumerate(num):
                    newCol = M - len(num) + k
                    grid[i][newCol] = [num, num_pos]
                num = ''
        # check adjacency for each gear
        total = 0
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        for i, j in gear_pos:
            seen = set()
            adj_num = 0
            gear_ratio = 1
            for row, col in direction:
                newRow = i + row
                newCol = j + col
                if (newRow, newCol) not in seen and newRow >= 0 and newRow < N and newCol >= 0 and newCol < M and grid[newRow][newCol]:
                    val = grid[newRow][newCol]
                    if isinstance(val, list):
                        adj_num += 1
                        gear_ratio *= int(val[0])
                        seen.update(val[1])
            if adj_num == 2:
                total += gear_ratio
        return total

print(solution())