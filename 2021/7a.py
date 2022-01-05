def solution():
    initialFile = ''
    with open('7.in', 'r') as file:
        initialFile = file.read()

    initialFile = initialFile.split(',')
    initialFile = list(map(int, initialFile))

    minGasVal = 2147483647
    for pos1 in initialFile:
        sum = 0
        for pos2 in initialFile:
            sum += abs(pos1 - pos2)
        if sum < minGasVal:
            minGasVal = sum

    print(minGasVal)


solution()

# post-problem realization: calculate the median!
