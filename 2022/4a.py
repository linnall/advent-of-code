def solution():
    with open("4.in", "r") as file:
        lines = file.read().split("\n")
        overlaps = 0
        for line in lines:
            interval1, interval2 = line.split(",")
            b1, e1 = map(int, interval1.split("-"))
            b2, e2 = map(int, interval2.split("-"))
            if (b1 <= b2 and e2 <= e1) or (b2 <= b1 and e1 <= e2):
                overlaps += 1
        return overlaps


print(solution())
