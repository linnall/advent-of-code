from typing import List


def add_vertical_line(dict, p1: List[int], p2: List[int]):
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


def add_horizontal_line(dict, p1: int, p2: int):
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


def add_diagonal_line(dict, p1: int, p2: int):
    x1, y1 = p1
    x2, y2 = p2
    yDiff = 0
    lowestX = min(x1, x2)
    yIncr = 0
    if x2 < x1:
        yDiff = y1 - y2
        yIncr = y2
    else:
        yDiff = y2 - y1
        yIncr = y1

    if yDiff < 0:
        for i in range(lowestX, lowestX + abs(x1 - x2) + 1):
            keyString = str(i) + ',' + str(yIncr)
            if keyString in dict:
                dict[keyString] += 1
            else:
                dict[keyString] = 1
            yIncr -= 1
    else:
        # yDiff > 0
        for i in range(lowestX, lowestX + abs(x1 - x2) + 1):
            keyString = str(i) + ',' + str(yIncr)
            if keyString in dict:
                dict[keyString] += 1
            else:
                dict[keyString] = 1
            yIncr += 1


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
                add_vertical_line(pointsDict, [x1, y1], [x2, y2])
            elif y1 == y2:
                # add horizontal
                add_horizontal_line(pointsDict, [x1, y1], [x2, y2])
            else:
                add_diagonal_line(pointsDict, [x1, y1], [x2, y2])

    for times in pointsDict.values():
        if times >= 2:
            ret += 1

    print(ret)


solution()
