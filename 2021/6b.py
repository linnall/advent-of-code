# solution inspo: https://zonito.medium.com/lantern-fish-day-6-advent-of-code-2021-python-solution-4444387a8380

def solution():
    entireFile = ''
    with open('6.in', 'r') as file:
        entireFile = file.read()

    initialList = entireFile.split(',')
    initialList = list(map(int, initialList))

    days = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for dayNum in initialList:
        days[dayNum] += 1

    for i in range(256):
        index = i % 9
        if days[index] > 0:
            # move current number of fish to index + 6 % 9
            adultFishNum = days[index]
            days[index] = 0
            days[(index + 7) % 9] += adultFishNum
            # add adultFishNum of babies to index + 8 % 9
            days[(index + 9) % 9] += adultFishNum

    print(sum(days))


solution()
