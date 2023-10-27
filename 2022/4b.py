def solution():
    with open("4.in", "r") as file:
        overlaps = 0
        lines = file.read().split("\n")
        for line in lines:
            interval1, interval2 = line.split(",")
            b1, e1 = map(int, interval1.split("-"))
            b2, e2 = map(int, interval2.split("-"))
            if b1 < b2:
                if e1 >= b2:
                    overlaps += 1
            else:
                if e2 >= b1:
                    overlaps += 1
        return overlaps


print(solution())
