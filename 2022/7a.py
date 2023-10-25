from collections import deque


class FileDirectory:
    def __init__(self, name, children, isFile=False, size=0):
        self.name = name
        self.isFile = isFile
        self.size = size
        self.children = children


CMD = "$"


def buildTree(instructions, node):
    if not instructions:
        return
    instruction = instructions.popleft().split()
    if instruction[0] == "$":
        if instruction[1] == "cd":
            _, cd, dir = instruction
            if dir == "..":
                return
            else:
                buildTree(instructions, node.children[dir])
        elif instruction[1] == "ls":
            currInstruction = instructions.popleft().split()
            while currInstruction[0] != "$":
                term1, term2 = currInstruction
                if term1 == "dir":
                    node.children[term2] = FileDirectory(term2, {})
                else:
                    node.children[term2] = FileDirectory(term2, {}, True, int(term1))
                if not instructions:
                    break
                currInstruction = instructions.popleft().split()
            _, cd, dir = currInstruction
            if dir == "..":
                return
            buildTree(instructions, node.children[dir])


def getDirectorySizes(root, targetDirectories):
    if root.isFile:
        return root.size
    else:
        directorySize = 0
        print(root.name, root.children.keys())
        for key, child in root.children.items():
            directorySize += getDirectorySizes(child, targetDirectories)
        if directorySize <= 100000:
            targetDirectories.append(directorySize)
        root.size = directorySize
        return directorySize


def solution():
    root = FileDirectory("/", {})
    with open("7.in", "r") as file:
        lines = deque(file.read().split("\n"))
        lines.popleft()
        buildTree(lines, root)
        targetDirectories = []
        getDirectorySizes(root, targetDirectories)
        print(targetDirectories)
        return sum(targetDirectories)


print(solution())
