def solution():
    start = [0, 0]
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
                prevx, prevy = head
                head = [head[0] + x, head[1] + y]
                hx, hy = head
                tx, ty = tail
                # diagonal case
                if (abs(hx - tx) == 2 and abs(hy - ty) > 0) or (
                    abs(hy - ty) == 2 and abs(hx - tx) > 0
                ):
                    tail = [prevx, prevy]
                    print("prev", tail)
                    tailPositions.add(tuple(tail))
                # horizontal or vertical case
                elif abs(hx - tx) > 1 or abs(hy - ty) > 1:
                    tail = [tx + x, ty + y]
                    print("in-line", tail)
                    tailPositions.add(tuple(tail))
        print(tailPositions)
        return len(tailPositions)
    # (-3, 2) does NOT belong!


print(solution())
