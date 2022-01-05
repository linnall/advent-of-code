import math


def compute_gas(steps):
    return (steps + 1) * steps / 2


def solution():
    initialFile = ''
    with open('7.in', 'r') as file:
        initialFile = file.read()

    initialFile = initialFile.split(',')
    initialFile = list(map(int, initialFile))

    minGasVal = 2147483647
    for pos1 in range(min(initialFile), max(initialFile) + 1):
        sum = 0
        for pos2 in initialFile:
            sum += compute_gas(abs(pos1 - pos2))
        if sum < minGasVal:
            minGasVal = sum

    print(minGasVal)


solution()

# post-problem realization: use the mean of the input numbers
