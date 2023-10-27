def moveTail(head, tail):
    hx, hy = head
    tx, ty = tail
    if abs(hx - tx) > 1 or abs(hy - ty) > 1:
        x, y = [
            (hx - tx) // abs(hx - tx) if hx - tx != 0 else 0,
            (hy - ty) // abs(hy - ty) if hy - ty != 0 else 0,
        ]
        return [tx + x, ty + y]
    else:
        return tail


def solution():
    with open("9.in", "r") as file:
        lines = file.read().split("\n")
        tailPositions = set([(0, 0)])
        directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
        head = [0, 0]
        tail = [0, 0]
        for line in lines:
            direction, paces = line.split()
            x, y = directions[direction]
            for _ in range(int(paces)):
                head = [head[0] + x, head[1] + y]
                print("head", head)
                tail = moveTail(head, tail)
                tailPositions.add(tuple(tail))
        print(tailPositions)
        return len(tailPositions)


print(solution())
