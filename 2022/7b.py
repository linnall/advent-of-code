from collections import defaultdict


sizes = defaultdict(int)


def solution():
    total = 0
    with open("7.in", "r") as file:
        lines = file.read().split("\n")
        paths = []
        for line in lines:
            line = line.split()
            if line[1] == "cd":
                _, cd, dir = line
                if dir == "..":
                    paths.pop()
                else:
                    paths.append(dir)
            elif line[1] == "ls":
                continue
            elif line[0] == "dir":
                continue
            else:
                size, filename = line
                for i in range(len(paths), -1, -1):
                    path = "/".join(paths[0:i])
                    sizes[path] += int(size)
        usedSpace = max(sizes.values())
        minDirSize = 70000000
        for sz in sizes.values():
            if usedSpace - sz <= 40000000:
                minDirSize = min(sz, minDirSize)
        return minDirSize


print(solution())
