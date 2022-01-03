from typing import List


def addVerticalLine(dict, p1: List[int], p2: List[int]):
    x1, y1 = p1
    y2 = p2[1]
    lowest = min(y1, y2)
    # p1 stays constant
    for i in range(lowest, lowest + abs(y1 - y2) + 1):
        keyString = str(x1) + ',' + str(i)
        if keyString in dict:
            dict[keyString] += 1
        else:
            dict[keyString] = 1


def addHorizontalLine(dict, p1: int, p2: int):
    x1, y1 = p1
    x2 = p2[0]
    lowest = min(x1, x2)
    # p1 stays constant
    for i in range(lowest, lowest + abs(x1 - x2) + 1):
        keyString = str(i) + ',' + str(y1)
        if keyString in dict:
            dict[keyString] += 1
        else:
            dict[keyString] = 1


def solution():
    # 'p1,p2' -> number of times it has been covered by lines
    pointsDict = {}
    ret = 0
    with open('5.in', 'r') as file:
        for line in file:
            # 0,9 -> 5,9
            listOfCoor = line.replace(' -> ', ',').split(',')
            x1 = int(listOfCoor[0])
            y1 = int(listOfCoor[1])
            x2 = int(listOfCoor[2])
            y2 = int(listOfCoor[3])

            if x1 == x2:
                # add vertical
                addVerticalLine(pointsDict, [x1, y1], [x2, y2])

            if y1 == y2:
                # add horizontal
                addHorizontalLine(pointsDict, [x1, y1], [x2, y2])

    for times in pointsDict.values():
        if times >= 2:
            ret += 1

    print(ret)


solution()
