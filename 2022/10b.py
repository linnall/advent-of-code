from collections import deque


def solution():
    with open("10.in", "r") as file:
        instructions = deque(file.read().split("\n"))
        X = 1
        verticalOffset = 0
        target = 39
        buffer = deque()
        for i in range(240):
            if i >= X + verticalOffset - 1 and i <= X + verticalOffset + 1:
                print("#", end="")
            else:
                print(".", end="")
            if i == target:
                print("\n", end="")
                target += 40
                verticalOffset += 40
            if instructions:
                line = instructions.popleft().split()
                if line[0] == "addx":
                    buffer.extend([0, int(line[1])])
                else:
                    buffer.append(0)
            if buffer:
                X += buffer.popleft()


solution()
