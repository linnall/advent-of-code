from collections import deque


def setUp(stacks, initialSetUp):
    lines = initialSetUp.split("\n")
    for line in lines:
        if "1" in line:
            break
        cratesAtLevel = [line[i : i + 4] for i in range(0, len(line), 4)]
        for i, crate in enumerate(cratesAtLevel):
            if "[" in crate and i + 1 in stacks:
                stacks[i + 1].append(crate[1])
            elif "[" in crate:
                stacks[i + 1] = deque([crate[1]])
    return stacks


def applyInstructions(instructions, stacks):
    for instruction in instructions:
        _, numOfCrates, _, dest, _, target = instruction.split(" ")
        for _ in range(int(numOfCrates)):
            crate = stacks[int(dest)].popleft()
            if int(target) not in stacks:
                stacks[int(target)] = deque()
            stacks[int(target)].appendleft(crate)


def solution():
    message = []
    with open("5.in", "r") as file:
        initialSetUp, instructions = file.read().split("\n\n")
        stacks = {}
        setUp(stacks, initialSetUp)
        applyInstructions(instructions.split("\n"), stacks)
        for i in range(len(initialSetUp.split("\n")[0]) // 4 + 1):
            message.append(stacks[i + 1][0])
    return "".join(message)


print(solution())
