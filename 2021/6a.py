'''
idea:
-parse initial input
-in a loop iterating 80 times 
-subtract days of life and add fish as necessary
'''


def solution():
    entireFile = ''
    with open('6.in', 'r') as file:
        entireFile = file.read()

    initialList = entireFile.split(',')
    initialList = list(map(int, initialList))

    # 80 days
    for i in range(80):
        enumerateList = initialList.copy()
        for i, fishDay in enumerate(enumerateList):
            if fishDay - 1 >= 0:
                initialList[i] -= 1
            else:
                initialList[i] = 6
                initialList.append(8)
        # print(initialList)
    print(len(initialList))


solution()
