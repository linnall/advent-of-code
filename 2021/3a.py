def solution():
    bitDict = {}
    gamma = ''
    delta = ''
    fileLines = 0
    with open('3.in', 'r') as file:
        for line in file:
            fileLines += 1
            for pos in range(len(line)-1):
                posInt = int(pos)
                if posInt in bitDict:
                    bitDict[posInt] += int(line[posInt])
                else:
                    bitDict[posInt] = int(line[posInt])
    for sum in bitDict.values():
        if sum * 2 < fileLines:
            gamma += '0'
            delta += '1'
        else:
            gamma += '1'
            delta += '0'
    print(int(gamma, 2) * int(delta, 2))


solution()
