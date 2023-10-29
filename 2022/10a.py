from collections import deque


def solution():
    with open("10.in", "r") as file:
        instructions = deque(file.read().split("\n"))
        signalStrength = 0
        X = 1
        target = 20
        buffer = deque()
        for i in range(1, 221):
            if i == target:
                signalStrength += X * i
                target += 40
            if instructions:
                line = instructions.popleft().split()
                if line[0] == "addx":
                    buffer.extend([0, int(line[1])])
                else:
                    buffer.append(0)
            if buffer:
                X += buffer.popleft()
    return signalStrength


print(solution())
